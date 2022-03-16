# MIT License
#
# Copyright (c) 2022 juggledev
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# https://github.com/relspas/siteswap-english-words
# @relspas
# Unlicense
def isValidSiteswap(s):
    d = set()
    n = len(s)
    for i in range(n):
        d.add((ord(s[i])+i)%n)
    if len(d) == len(s):
        return True
    return False

# https://stackoverflow.com/a/52323807
# @q-qiao
# CC BY-SA 4.0
def isValidDate(d, m):
    days_in_month = [
        0,  # None
        31, # Jan
        29, # Feb
        31, # Mar
        30, # Apr
        31, # May
        30, # Jun
        31, # Jul
        31, # Aug
        30, # Sep
        31, # Oct
        30, # Nov
        31  # Dec
    ]
    if 0 < d <= days_in_month[m]:
        return True
    else:
        return False

def numObjects(s):
    # Only works for vanilla siteswaps with values less than 10
    return int(sum([int(i) for i in list(s)]) / len(s))
    

ss_dates = set()

print("M/D")
for month in range(1, 12+1):
    for day in range(1, 31+1):
        ss = str(month) + str(day)
        if isValidSiteswap(ss):
            ss_dates.add(ss)
            print(f"    {month}/{day} ({numObjects(ss)} objects)")

print("MM/DD")
for month in range(1, 12+1):
    for day in range(1, 31+1):
        m_str = str(month).rjust(2, "0")
        d_str = str(day).rjust(2, "0")
        ss = str(month).rjust(2, "0") + str(day).rjust(2, "0")
        if isValidSiteswap(ss):
            ss_dates.add(ss)
            print(f"    {m_str}/{d_str} ({numObjects(ss)} objects)")

print("D/M")
for day in range(1, 31+1):
    for month in range(1, 12+1):
        ss = str(day) + str(month)
        if isValidSiteswap(ss):
            ss_dates.add(ss)
            print(f"    {day}/{month} ({numObjects(ss)} objects)")

print("DD/MM")
for day in range(1, 31+1):
    for month in range(1, 12+1):
        m_str = str(month).rjust(2, "0")
        d_str = str(day).rjust(2, "0")
        ss = str(day).rjust(2, "0") + str(month).rjust(2, "0")
        if isValidSiteswap(ss):
            ss_dates.add(ss)
            print(f"    {d_str}/{m_str} ({numObjects(ss)} objects)")

# print(f"Set ({len(ss_dates)}):")
# print(ss_dates)
