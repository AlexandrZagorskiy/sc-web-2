# -*- coding: utf-8 -*-

from . import base
import decorators


@decorators.class_logging
class MainHandler(base.BaseHandler):
    def get(self):
        first_time = self.get_cookie("first_time", "!")
        self.set_cookie("first_time", "0")
        self.render("base.html", has_entered = False, user = self.current_user, first_time = first_time)
