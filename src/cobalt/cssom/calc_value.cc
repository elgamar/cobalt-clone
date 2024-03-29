// Copyright 2015 The Cobalt Authors. All Rights Reserved.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

#include "cobalt/cssom/calc_value.h"

#include "base/stringprintf.h"
#include "cobalt/cssom/property_value_visitor.h"

namespace cobalt {
namespace cssom {

void CalcValue::Accept(PropertyValueVisitor* visitor) {
  visitor->VisitCalc(this);
}

std::string CalcValue::ToString() const {
  return base::StringPrintf("calc(%s + %s)", length_value_->ToString().c_str(),
                            percentage_value_->ToString().c_str());
}

}  // namespace cssom
}  // namespace cobalt
