// Copyright 2017 Google Inc. All Rights Reserved.
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
#ifndef COBALT_BASE_C_VAL_COLLECTION_ENTRY_STATS_H_
#define COBALT_BASE_C_VAL_COLLECTION_ENTRY_STATS_H_

#include <algorithm>
#include <cmath>
#include <numeric>
#include <sstream>
#include <string>
#include <vector>

#include "base/callback.h"
#include "base/logging.h"
#include "base/stringprintf.h"
#include "base/time.h"
#include "cobalt/base/c_val.h"
#include "cobalt/base/unused.h"

namespace base {
namespace CValDetail {

// This class tracks a collection of entries, which it retains in memory. When
// either the max size of the collection is reached or Flush() is manually
// called, the count, average, minimum, maximum, 25th, 50th, 75th and 95th
// percentiles, and standard deviation of the collection are recorded with
// CVals, and the tracking resets in preparation for the next collection of
// entries.
// NOTE1: By default there is no max size and the collection will continue to
//        grow indefinitely until Flush() is called.
// NOTE2: This class keeps all of the entries in memory until flush is called so
//        that percentiles can be determined. In cases where the number of
//        entries is extremely large, |CValTimeIntervalEntryStats| is more
//        appropriate, as it does its tracking without keeping entries in memory
//        (at the cost of not being able to provide percentiles);
// NOTE3: This class provides the ability to record all entries within a single
//        string CVal when |enable_entry_list_c_val| is set to true in the
//        constructor. By default, this CVal is not used.
template <typename EntryType, typename Visibility = CValDebug>
class CValCollectionEntryStatsImpl {
 public:
  static const size_t kNoMaxSize = 0;

  struct FlushResults {
    FlushResults(size_t sample_count, EntryType average, EntryType minimum,
                 EntryType maximum, EntryType standard_deviation,
                 EntryType percentile_25th, EntryType percentile_50th,
                 EntryType percentile_75th, EntryType percentile_95th)
        : sample_count(sample_count),
          average(average),
          minimum(minimum),
          maximum(maximum),
          standard_deviation(standard_deviation),
          percentile_25th(percentile_25th),
          percentile_50th(percentile_50th),
          percentile_75th(percentile_75th),
          percentile_95th(percentile_95th) {}

    size_t sample_count;
    EntryType average;
    EntryType minimum;
    EntryType maximum;
    EntryType standard_deviation;
    EntryType percentile_25th;
    EntryType percentile_50th;
    EntryType percentile_75th;
    EntryType percentile_95th;
  };

  typedef base::Callback<void(const FlushResults&)> OnFlushCallback;

  CValCollectionEntryStatsImpl(
      const std::string& name, size_t max_size = kNoMaxSize,
      bool enable_entry_list_c_val = false,
      const OnFlushCallback& on_flush = OnFlushCallback());

  // Add an entry to the collection. This may trigger a Flush() if adding the
  // entry causes the max size to be reached.
  void AddEntry(const EntryType& value);
  // Manually flush the collection's entries. This updates the stat cvals and
  // clears the entries.
  void Flush();

 private:
  typedef std::vector<EntryType> CollectionType;

  static EntryType CalculatePercentile(const CollectionType& sorted_collection,
                                       int percentile);
  static double CalculateStandardDeviation(const CollectionType& collection,
                                           double mean);

  // Constructs a string representing the entries within the collection and
  // populates |entry_list_| with it if the entry list CVal was enabled during
  // construction.
  void PopulateEntryList();

  // The maximum size of the collection before Flush() is automatically called.
  const size_t max_size_;

  // Callback to call whenever the values are flushed.
  const OnFlushCallback on_flush_;

  // The current collection of entries. These will be used to generate the cval
  // stats during the next call of Flush().
  CollectionType collection_;

  // CVals of the stats for the previous collection.
  base::CVal<size_t, Visibility> count_;
  base::CVal<EntryType, Visibility> average_;
  base::CVal<EntryType, Visibility> minimum_;
  base::CVal<EntryType, Visibility> maximum_;
  base::CVal<EntryType, Visibility> percentile_25th_;
  base::CVal<EntryType, Visibility> percentile_50th_;
  base::CVal<EntryType, Visibility> percentile_75th_;
  base::CVal<EntryType, Visibility> percentile_95th_;
  base::CVal<EntryType, Visibility> standard_deviation_;
  // |entry_list_| is only non-NULL when it is enabled.
  scoped_ptr<base::CVal<std::string, Visibility> > entry_list_;
};

template <typename EntryType, typename Visibility>
CValCollectionEntryStatsImpl<EntryType, Visibility>::
    CValCollectionEntryStatsImpl(
        const std::string& name, size_t max_size /*=kNoMaxSize*/,
        bool enable_entry_list_c_val /*=false*/,
        const OnFlushCallback& on_flush /*=OnFlushCallback()*/)
    : max_size_(max_size),
      on_flush_(on_flush),
      count_(StringPrintf("%s.Cnt", name.c_str()), 0, "Total entries."),
      average_(StringPrintf("%s.Avg", name.c_str()), EntryType(),
               "Average value."),
      minimum_(StringPrintf("%s.Min", name.c_str()), EntryType(),
               "Minimum value."),
      maximum_(StringPrintf("%s.Max", name.c_str()), EntryType(),
               "Maximum value."),
      percentile_25th_(StringPrintf("%s.Pct.25th", name.c_str()), EntryType(),
                       "25th percentile value."),
      percentile_50th_(StringPrintf("%s.Pct.50th", name.c_str()), EntryType(),
                       "50th percentile value."),
      percentile_75th_(StringPrintf("%s.Pct.75th", name.c_str()), EntryType(),
                       "75th percentile value."),
      percentile_95th_(StringPrintf("%s.Pct.95th", name.c_str()), EntryType(),
                       "95th percentile value."),
      standard_deviation_(StringPrintf("%s.Std", name.c_str()), EntryType(),
                          "Standard deviation of values.") {
  if (enable_entry_list_c_val) {
    entry_list_.reset(new base::CVal<std::string, Visibility>(
        StringPrintf("%s.EntryList", name.c_str()), "[]",
        "The list of entries in the collection."));
  }
}

template <typename EntryType, typename Visibility>
void CValCollectionEntryStatsImpl<EntryType, Visibility>::AddEntry(
    const EntryType& value) {
  collection_.push_back(value);
  if (collection_.size() == max_size_) {
    Flush();
  }
}

template <typename EntryType, typename Visibility>
void CValCollectionEntryStatsImpl<EntryType, Visibility>::Flush() {
  if (collection_.size() == 0) {
    return;
  }

  // Populate the entry list cval before the collection is sorted.
  PopulateEntryList();

  // Sort the collection. This allows min, max, and percentiles to be easily
  // determined.
  std::sort(collection_.begin(), collection_.end());

  // Calculate the mean of the collection.
  EntryType sum = std::accumulate(collection_.begin(), collection_.end(),
                                  CValDetail::FromDouble<EntryType>(0));
  double mean = CValDetail::ToDouble<EntryType>(sum) / collection_.size();

  // Update the collection stat cvals.
  size_t count = collection_.size();
  EntryType average = CValDetail::FromDouble<EntryType>(mean);
  EntryType minimum = collection_.front();
  EntryType maximum = collection_.back();
  EntryType percentile_25th = CalculatePercentile(collection_, 25);
  EntryType percentile_50th = CalculatePercentile(collection_, 50);
  EntryType percentile_75th = CalculatePercentile(collection_, 75);
  EntryType percentile_95th = CalculatePercentile(collection_, 95);
  EntryType standard_deviation = CValDetail::FromDouble<EntryType>(
      CalculateStandardDeviation(collection_, mean));

  // Flush the computed values out to the CVals.
  count_ = count;
  average_ = average;
  minimum_ = minimum;
  maximum_ = maximum;
  percentile_25th_ = percentile_25th;
  percentile_50th_ = percentile_50th;
  percentile_75th_ = percentile_75th;
  percentile_95th_ = percentile_95th;
  standard_deviation_ = standard_deviation;

  collection_.clear();

  // Callback to any listeners with the flush values.
  if (!on_flush_.is_null()) {
    on_flush_.Run(FlushResults(
        count, average, minimum, maximum, standard_deviation, percentile_25th,
        percentile_50th, percentile_75th, percentile_95th));
  }
}

template <typename EntryType, typename Visibility>
EntryType
CValCollectionEntryStatsImpl<EntryType, Visibility>::CalculatePercentile(
    const CollectionType& sorted_collection, int percentile) {
  DCHECK_GT(sorted_collection.size(), 0);
  DCHECK(percentile >= 0 && percentile <= 100);

  // Determine the position of the percentile within the collection.
  double percentile_position =
      (sorted_collection.size() - 1) * static_cast<double>(percentile) * 0.01;

  // Split out the integral and fractional parts of the percentile position.
  double percentile_integral_position, percentile_fractional_position;
  percentile_fractional_position =
      std::modf(percentile_position, &percentile_integral_position);

  int percentile_first_index = static_cast<int>(percentile_integral_position);

  // If |percentile_first_index| maps to the last entry, then there is no
  // second entry and there's nothing to interpolate; simply use the last entry.
  if (sorted_collection.size() == percentile_first_index + 1) {
    return sorted_collection.back();
  }

  // Interpolate between the two entries that the percentile falls between.
  double first_data_point = CValDetail::ToDouble<EntryType>(
                                sorted_collection[percentile_first_index]) *
                            (1.0 - percentile_fractional_position);
  double second_data_point =
      CValDetail::ToDouble<EntryType>(
          sorted_collection[percentile_first_index + 1]) *
      percentile_fractional_position;

  return CValDetail::FromDouble<EntryType>(first_data_point +
                                           second_data_point);
}

template <typename EntryType, typename Visibility>
double
CValCollectionEntryStatsImpl<EntryType, Visibility>::CalculateStandardDeviation(
    const CollectionType& collection, double mean) {
  if (collection.size() <= 1) {
    return 0;
  }

  double dif_squared_sum = 0;
  for (size_t i = 0; i < collection.size(); ++i) {
    double dif = CValDetail::ToDouble<EntryType>(collection[i]) - mean;
    dif_squared_sum += dif * dif;
  }

  double variance =
      dif_squared_sum / static_cast<double>(collection.size() - 1);

  return std::sqrt(variance);
}

template <typename EntryType, typename Visibility>
void CValCollectionEntryStatsImpl<EntryType, Visibility>::PopulateEntryList() {
  // If the entry list was not enabled, then |entry_list_| will be NULL and
  // there is nothing to do. Simply return.
  if (!entry_list_) {
    return;
  }

  // Construct a string containing a list representation of the collection
  // entries and set the entry list CVal to it.
  std::ostringstream oss;
  oss << "[";
  for (size_t i = 0; i < collection_.size(); ++i) {
    if (i > 0) {
      oss << ", ";
    }
    oss << CValDetail::ValToString<EntryType>(collection_[i]);
  }
  oss << "]";
  *entry_list_ = oss.str();
}

#if !defined(ENABLE_DEBUG_C_VAL)
// This is a stub class that disables CValCollectionEntryStats when
// ENABLE_DEBUG_C_VAL is not defined.
template <typename EntryType>
class CValCollectionEntryStatsStub {
 public:
  typedef base::Unused FlushResults;
  typedef base::Unused OnFlushCallback;

  explicit CValCollectionEntryStatsStub(const std::string& name) {
    UNREFERENCED_PARAMETER(name);
  }
  CValCollectionEntryStatsStub(
      const std::string& name, size_t max_size, bool enable_entry_list_c_val,
      const OnFlushCallback& on_flush = OnFlushCallback()) {
    UNREFERENCED_PARAMETER(name);
    UNREFERENCED_PARAMETER(max_size);
    UNREFERENCED_PARAMETER(enable_entry_list_c_val);
    UNREFERENCED_PARAMETER(on_flush);
  }

  void AddEntry(const EntryType& value) { UNREFERENCED_PARAMETER(value); }
  void Flush() {}
};
#endif  // ENABLE_DEBUG_C_VAL

}  // namespace CValDetail

template <typename EntryType, typename Visibility = CValDebug>
class CValCollectionEntryStats {};

template <typename EntryType>
#if defined(ENABLE_DEBUG_C_VAL)
// When ENABLE_DEBUG_C_VAL is defined, CVals with Visibility set to CValDebug
// are tracked through the CVal system.
class CValCollectionEntryStats<EntryType, CValDebug>
    : public CValDetail::CValCollectionEntryStatsImpl<EntryType, CValDebug> {
  typedef CValDetail::CValCollectionEntryStatsImpl<EntryType, CValDebug>
      CValParent;
#else   // ENABLE_DEBUG_C_VAL
// When ENABLE_DEBUG_C_VAL is not defined, CVals with Visibility set to
// CValDebug are not tracked though the CVal system and
// CValCollectionEntryStats can be stubbed out.
class CValCollectionEntryStats<EntryType, CValDebug>
    : public CValDetail::CValCollectionEntryStatsStub<EntryType> {
  typedef CValDetail::CValCollectionEntryStatsStub<EntryType> CValParent;
#endif  // ENABLE_DEBUG_C_VAL

 public:
  typedef typename CValParent::OnFlushCallback OnFlushCallback;
  typedef typename CValParent::FlushResults FlushResults;

  explicit CValCollectionEntryStats(const std::string& name)
      : CValParent(name) {}
  CValCollectionEntryStats(const std::string& name, size_t max_size,
                           bool enable_entry_list_c_val,
                           const OnFlushCallback& on_flush = OnFlushCallback())
      : CValParent(name, max_size, enable_entry_list_c_val, on_flush) {}
};

// CVals with visibility set to CValPublic are always tracked though the CVal
// system, regardless of the ENABLE_DEBUG_C_VAL state.
template <typename EntryType>
class CValCollectionEntryStats<EntryType, CValPublic>
    : public CValDetail::CValCollectionEntryStatsImpl<EntryType, CValPublic> {
  typedef CValDetail::CValCollectionEntryStatsImpl<EntryType, CValPublic>
      CValParent;

 public:
  typedef typename CValParent::OnFlushCallback OnFlushCallback;
  typedef typename CValParent::FlushResults FlushResults;

  explicit CValCollectionEntryStats(const std::string& name)
      : CValParent(name) {}
  CValCollectionEntryStats(const std::string& name, size_t max_size,
                           bool enable_entry_list_c_val,
                           const OnFlushCallback& on_flush = OnFlushCallback())
      : CValParent(name, max_size, enable_entry_list_c_val, on_flush) {}
};

}  // namespace base

#endif  // COBALT_BASE_C_VAL_COLLECTION_ENTRY_STATS_H_
