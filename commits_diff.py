#!/usr/bin/pyhton

from __future__ import print_function

import sys


def parse_log(name):
    changes = {}
    with open(name, "r") as log:
        expect_title = False
        expect_change_id = False
        title = ''
        for line in (x.strip() for x in log):
            if line.startswith("Date: "):
                expect_title = True
                continue

            if expect_title and line:
                title = line
                expect_title = False
                expect_change_id = True
            elif expect_change_id and line.startswith("Change-Id:"):
                change_id = line[line.find(':') + 1:].strip()
                expect_change_id = False
                if not title.startswith('Merge "'):
                    changes[change_id] = title
                else:
                    print(change_id, title)
                title = ''
    return changes

master_changes = parse_log(sys.argv[1])
stable_changes = parse_log(sys.argv[2])


def print_change(change_id, title, in_master):
    link = 'https://review.openstack.org/#/q/{0}'.format(change_id)
    title = '"{0}"'.format(title)
    print(link, change_id, title, int(in_master), int(not in_master), sep=',')

print ("master:")
for change in master_changes:
    if change not in stable_changes:
        print_change(change, master_changes[change], True)

print('\n\n')
print("stable:")
for change in stable_changes:
    if change not in master_changes:
        print_change(change, stable_changes[change], False)
