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


class PendingMessageModel(Base):
    __tablename__ = 'media_pending_message'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    trigger_id = Column(String(50))
    content = Column(Text())
    pre_info = Column(Text())


engine = create_engine(THANOSDB_URL)
Session = sessionmaker(bind=engine)


def foo(i):
    i = str(i)
    db_session = Session()
    pending_msg = PendingMessageModel(trigger_id='test_'+i)
    db_session.add(pending_msg)
    db_session.commit()
    # db_session.close()

    # db_session = Session()
    pending_message = db_session.query(PendingMessageModel).filter(
        PendingMessageModel.trigger_id == 'test_'+i).first()

    pending_message.content = i
    db_session.add(pending_msg)
    db_session.commit()
    pending_message
    print i
    if pending_message:
        pending_message.id
    db_session.close()


def delete():
    db_session = Session()
    db_session.query(PendingMessageModel).filter(
        PendingMessageModel.trigger_id.contains('test')).delete(synchronize_session=False)

    db_session.commit()
    db_session.close()


# session_list = []
# for i in range(0, 1000):
#     session_list.append(gevent.spawn(foo, i))


gevent.joinall(session_list)
# delete()
