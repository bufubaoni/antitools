#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from gevent import monkey
monkey.patch_all()  # noqa
import time
import gevent

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, Text, Sequence, String
from sqlalchemy.ext.declarative import declarative_base

metadata = MetaData()
Base = declarative_base(metadata=metadata)
THANOSDB_URL = ''


class PendingMessageModel(Base):
    __tablename__ = 'media_pending_message'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    trigger_id = Column(String(50))
    content = Column(Text())
    pre_info = Column(Text())


engine = create_engine(THANOSDB_URL)


def foo(i):

    Session = sessionmaker(bind=engine)
    db_session = Session()

    pending_message = db_session.query(PendingMessageModel).filter(
        PendingMessageModel.id == i).first()
    db_session.commit()

    print i
    if pending_message:
        pending_message.id

    db_session.close()
    Session.close_all()


session_list = []
for i in range(0, 10000):
    session_list.append(gevent.spawn(foo, i))

gevent.joinall(session_list)
