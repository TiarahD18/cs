// Copyright 2018 Google LLC
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

// Use querySelector to store the div in a variable.

let txt = " ";
let a = [1,2,3,4,5];
let b = [];

function test1(value, index, array)
{
  txt = txt + value + " ";
}

function test2(value, index, array)
{
  txt = txt + index + " ";
}

function test3(value, index, array)
{
  if(index + 1 < array.length)
  {
    b.push(value + array[index + 1]);
  }
}
