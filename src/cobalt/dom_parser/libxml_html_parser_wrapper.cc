/*
 * Copyright 2015 Google Inc. All Rights Reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#include "cobalt/dom_parser/libxml_html_parser_wrapper.h"

#include "base/basictypes.h"
#include "base/string_util.h"
#include "cobalt/dom/element.h"
#include "cobalt/dom/html_script_element.h"

namespace cobalt {
namespace dom_parser {
namespace {

// Libxml SAX handler.
//   http://www.xmlsoft.org/html/libxml-tree.html#xmlSAXHandler

// NOTE: Please read about XXE attacks before implementing handler fields such
// as resolveEntity and entityDecl.
htmlSAXHandler html_sax_handler = {
    NULL,           /* internalSubset */
    NULL,           /* isStandalone */
    NULL,           /* hasInternalSubset */
    NULL,           /* hasExternalSubset */
    NULL,           /* resolveEntity */
    NULL,           /* getEntity */
    NULL,           /* entityDecl */
    NULL,           /* notationDecl */
    NULL,           /* attributeDecl */
    NULL,           /* elementDecl */
    NULL,           /* unparsedEntityDecl */
    NULL,           /* setDocumentLocator */
    &StartDocument, /* startDocument */
    &EndDocument,   /* endDocument */
    &StartElement,  /* startElement */
    &EndElement,    /* endElement */
    NULL,           /* reference */
    &Characters,    /* characters */
    NULL,           /* ignorableWhitespace */
    NULL,           /* processingInstruction */
    &Comment,       /* comment */
    &ParserWarning, /* xmlParserWarning */
    &ParserError,   /* xmlParserError */
    &ParserFatal,   /* xmlParserFatalError */
    NULL,           /* getParameterEntity */
    NULL,           /* cdataBlock */
    NULL,           /* externalSubset */
    1,              /* initialized */
    NULL,           /* private */
    NULL,           /* startElementNsSAX2Func */
    NULL,           /* endElementNsSAX2Func */
    NULL            /* xmlStructuredErrorFunc */
};

}  // namespace

//////////////////////////////////////////////////////////////////
// LibxmlHTMLParserWrapper
//////////////////////////////////////////////////////////////////

LibxmlHTMLParserWrapper::~LibxmlHTMLParserWrapper() {
  if (html_parser_context_) {
    htmlFreeParserCtxt(html_parser_context_);
  }
}

void LibxmlHTMLParserWrapper::OnStartElement(
    const std::string& name, const ParserAttributeVector& attributes) {
  // Implied tags generated by Libxml should be ignored when parsing fragment.
  if (!IsFullDocument() && (name == "html" || name == "body")) {
    return;
  }
  LibxmlParserWrapper::OnStartElement(name, attributes);
}

void LibxmlHTMLParserWrapper::OnEndElement(const std::string& name) {
  // Implied tags generated by Libxml should be ignored when parsing fragment.
  if (!IsFullDocument() && (name == "html" || name == "body")) {
    return;
  }

  // If the top if the node stack is an html script element, then set its
  // should_execute_ field to be our should_run_scripts_ field.
  DCHECK(!node_stack().empty());
  if (name == "script") {
    scoped_refptr<dom::HTMLScriptElement> html_script_element =
        node_stack().top()->AsElement()->AsHTMLElement()->AsHTMLScriptElement();
    DCHECK(html_script_element);
    html_script_element->set_should_execute(should_run_scripts_);
  }

  LibxmlParserWrapper::OnEndElement(name);
}

void LibxmlHTMLParserWrapper::DecodeChunk(const char* data, size_t size) {
  if (size == 0) {
    return;
  }

  std::string current_chunk;
  PreprocessChunk(data, size, &current_chunk);

  if (max_severity() == kFatal) {
    return;
  }

  if (!html_parser_context_) {
    // Suppress emitting a <p> element at the root level. This is needed to
    // prevent a <p> tag being added to text at the root level, for example
    // when used for setting an element's innerHTML.
    htmlEmitImpliedRootLevelParagraph(0);

    html_parser_context_ =
        htmlCreatePushParserCtxt(&html_sax_handler, this, current_chunk.c_str(),
                                 static_cast<int>(current_chunk.size()),
                                 NULL /*filename*/, XML_CHAR_ENCODING_UTF8);

    if (!html_parser_context_) {
      static const char kErrorUnableCreateParser[] =
          "Unable to create the libxml2 parser.";
      OnParsingIssue(kFatal, kErrorUnableCreateParser);
    } else {
      if (IsFullDocument()) {
        document()->IncreaseLoadingCounter();
      }
    }
  } else {
    DCHECK(html_parser_context_);
    htmlParseChunk(html_parser_context_, current_chunk.c_str(),
                   static_cast<int>(current_chunk.size()),
                   0 /*do not terminate*/);
  }
}

void LibxmlHTMLParserWrapper::Finish() {
  if (!html_parser_context_) {
    static const char empty_document[] = "<html><body></body></html>";
    DecodeChunk(empty_document, arraysize(empty_document));
  }

  if (html_parser_context_) {
    htmlParseChunk(html_parser_context_, NULL, 0,
                   1 /*terminate*/);  // Triggers EndDocument
    if (IsFullDocument()) {
      document()->DecreaseLoadingCounterAndMaybeDispatchLoadEvent();
    }
  }
}

base::SourceLocation LibxmlHTMLParserWrapper::GetSourceLocation() {
  base::SourceLocation source_location(first_chunk_location().file_path,
                                       html_parser_context_->input->line,
                                       html_parser_context_->input->col);
  base::AdjustForStartLocation(
      first_chunk_location().line_number, first_chunk_location().column_number,
      &source_location.line_number, &source_location.column_number);
  return source_location;
}

}  // namespace dom_parser
}  // namespace cobalt
