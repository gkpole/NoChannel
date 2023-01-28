#!/usr/bin/python
# -*- coding: utf-8 -*-
from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

class IsChannelFilter(BoundFilter):
    key = "is_channel"
    
    def __init__(self, is_channel):
        self.is_channel = is_channel
    
