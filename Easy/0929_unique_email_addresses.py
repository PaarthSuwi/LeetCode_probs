# ============================================================
# LeetCode 929 - Unique Email Addresses
# Difficulty: Easy
# ============================================================
#
# QUESTION:
# Every valid email has a local name and a domain name, separated by '@'.
# Rules for local name: dots ('.') are ignored; everything after '+' is ignored.
# Given a list of emails, return the number of different addresses that
# actually receive mails.
#
# Example:
#   Input:  emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com"]
#   Output: 2  (both normalize to "testemail@leetcode.com" -- wait, same)
#            Actually output: 1
#
# Constraints:
#   - 1 <= emails.length <= 100
#   - 1 <= emails[i].length <= 100
#   - emails[i] contain exactly one '@' character.
#
# ============================================================
# THEORY / APPROACH:
# Normalize each email: split by '@', process local name (remove dots,
# truncate at '+'), rejoin with domain. Use a set to count unique addresses.
#
# Time Complexity:  O(n * m)  — n = emails, m = avg email length
# Space Complexity: O(n * m)  — set storage
# ============================================================

from typing import List

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()
        for email in emails:
            local, domain = email.split('@')
            local = local.split('+')[0].replace('.', '')
            unique.add(local + '@' + domain)
        return len(unique)
