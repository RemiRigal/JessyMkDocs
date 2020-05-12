#!/usr/bin/env python
# coding: utf-8

import datetime
from string import Template
from os.path import dirname, join, abspath


class Report(object):

    TEMPLATE_FILE = join(dirname(dirname(abspath(__file__))), "docs", "assets", "templates", "report.md")

    def __init__(self, expType: str, params: list, notes: str = "Pas de notes"):
        with open(self.TEMPLATE_FILE, "r") as stream:
            self.template = Template(stream.read())
        self.args = {
            "DATE": datetime.datetime.now().isoformat(),
            "PARAMS": "\n- " + "\n- ".join([f"{p.name}: {p.value}" for p in params]),
            "TYPE": expType,
            "NOTES": notes
        }

    def saveReport(self, results: str):
        self.args["RESULTS"] = results
        reportFile = join(dirname(dirname(abspath(__file__))), "docs", "reports", f"report_{self.args['DATE']}.md")
        with open(reportFile, "w") as stream:
            stream.write(self.template.substitute(self.args))


class Param(object):

    def __init__(self, name, value):
        self.name = name
        self.value = value


if __name__ == "__main__":
    import random

    params = [
        Param("Super param", random.random() * 20),
        Param("Hello", random.randint(0, 100)),
        Param("Salut salut", "test")
    ]
    report = Report("traction mécanique", params)
    report.saveReport(f"Gain de {random.randint(110, 150)}% de performance.")
