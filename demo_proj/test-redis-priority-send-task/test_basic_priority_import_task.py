from time import sleep
from unittest import TestCase

from celery import chord, chain

from celery_proj.apps_end_by_string.task.main_task import main_task

# Priorities:   0, 3, 6, 9
# Queues:       a-high, b-medium, c-low


"""
NOTE:
This first task fired in each test must ALWAYS assumed to finish first. This
is because when the tasks fire, the queue is empty, so it has no other higher priority
"""


class TestPriority(TestCase):

    def test_simple(self):
        """
        Test a simple FIFO queue with priority (de)escalation
        """
        tasks = [
            {"priority": 0, "name": "A"},
            {"priority": 0, "name": "B"},
            {"priority": 0, "name": "C"},
            {"priority": 1, "name": "D"},  # deescalate
            {"priority": 0, "name": "E"},
            {"priority": 0, "name": "F"},
            {"priority": 1, "name": "G"},  # deescalate
            {"priority": 0, "name": "H"},
        ]
        results = []
        for task in tasks:
            t = main_task.s(task["name"])
            results.append(t.apply_async(priority=task["priority"]))

        complete = False
        success = []
        while not complete:
            complete = True
            for r in results:
                if r.state != "SUCCESS":
                    complete = False
                else:
                    v = r.result
                    if v[0] not in success:
                        success.append(v[0])
            sleep(1)

        self.assertEqual(
            success,
            ["A", "B", "C", "E", "F", "H", "D", "G"],
            "Numeric Priority not completed in expected order"
        )

    def testDefaultPriority(self):
        """
        Test a simple FIFO queue with priority (de)escalation
        """
        tasks = [
            {"priority": 0, "name": "A"},
            {"priority": 0, "name": "B"},
            {"priority": 0, "name": "C"},
            {"priority": 1, "name": "D"},  # deescalate
            {"priority": 0, "name": "E"},
            {"priority": 0, "name": "F"},
            {"priority": 1, "name": "G"},  # deescalate
            {"priority": 0, "name": "H"},
        ]
        results = []
        for task in tasks:
            t = main_task.s(task["name"])
            if task["priority"] == 1:
                results.append(t.apply_async())
            else:
                results.append(t.apply_async(priority=task["priority"]))

        complete = False
        success = []
        while not complete:
            complete = True
            for r in results:
                if r.state != "SUCCESS":
                    complete = False
                else:
                    v = r.result
                    if v[0] not in success:
                        success.append(v[0])
            sleep(1)

        self.assertEqual(
            success,
            ["A", "B", "C", "E", "F", "H", "D", "G"],
            "Numeric Priority not completed in expected order"
        )
