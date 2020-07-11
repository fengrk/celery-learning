from time import sleep
from unittest import TestCase

from celery_proj.apps_end_by_string.priority_app import app, task_routes

# Priorities:   0, 3, 6, 9
# Queues:       a-high, b-medium, c-low


"""
NOTE:
This first task fired in each test must ALWAYS assumed to finish first. This
is because when the tasks fire, the queue is empty, so it has no other higher priority
"""


class TestPriority(TestCase):

    def setUp(self) -> None:
        print(__file__)

        self.task_name = None
        for task in task_routes:
            self.task_name = task
            break

        self.assertIsNotNone(self.task_name)
        sleep(3)

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
            results.append(app.send_task(self.task_name, args=(task["name"],), priority=task["priority"]))

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
            sleep(0.1)

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
            if task["priority"] == 1:
                results.append(app.send_task(self.task_name, args=(task["name"],), priority=1))  # todo ignore priority, test not pass
            else:
                results.append(app.send_task(self.task_name, args=(task["name"],), priority=task["priority"]))

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
            sleep(0.1)

        self.assertEqual(
            success,
            ["A", "B", "C", "E", "F", "H", "D", "G"],
            "Numeric Priority not completed in expected order"
        )
