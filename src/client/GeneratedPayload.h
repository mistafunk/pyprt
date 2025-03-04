/**
 * PyPRT - Python Bindings for the Procedural Runtime (PRT) of CityEngine
 *
 * Copyright (c) 2012-2023 Esri R&D Center Zurich
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 * A copy of the license is available in the repository's LICENSE file.
 */

#pragma once

#include "types.h"

#include "pybind11/pybind11.h"

#include <memory>
#include <string>
#include <vector>

struct GeneratedPayload {
	Coordinates mVertices;
	Indices mIndices;
	Indices mFaces;
	pybind11::dict mCGAReport;
	std::wstring mCGAPrints;
	std::vector<std::wstring> mCGAErrors;
	pybind11::dict mAttrVal;
};

using GeneratedPayloadPtr = std::shared_ptr<GeneratedPayload>;