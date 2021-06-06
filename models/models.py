# coding: utf-8
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, Text, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Alias(Base):
    __tablename__ = 'aliases'

    id = Column(UUID, primary_key=True)
    alias = Column(String(255), nullable=False)
    description = Column(String(1024))


class ProcessingType(Base):
    __tablename__ = 'processing_types'

    id = Column(UUID, primary_key=True)
    processing_type = Column(String(255), nullable=False)
    description = Column(String(1024))


class RsDevice(Base):
    __tablename__ = 'rs_devices'

    id = Column(UUID, primary_key=True)
    rs_device = Column(String(255), nullable=False)
    description = Column(String(1024))


class Channel(Base):
    __tablename__ = 'channels'

    id = Column(UUID, primary_key=True)
    channel = Column(String(255))
    rs_device_id = Column(ForeignKey('rs_devices.id'), nullable=False, index=True)
    spatial_res = Column(Integer)
    unit = Column(String(255))
    description = Column(String(1024))
    special = Column(Boolean, nullable=False)
    formula = Column(Text)

    rs_device = relationship('RsDevice')


class Raster(Base):
    __tablename__ = 'rasters'

    id = Column(UUID, primary_key=True)
    alias = Column(ForeignKey('aliases.id'), nullable=False, index=True)
    info = Column(ForeignKey('channels.id'), index=True)
    sensing_time = Column(DateTime, nullable=False)
    processing_type = Column(ForeignKey('processing_types.id'), nullable=False, index=True)
    filepath = Column(String(255), nullable=False)

    alias1 = relationship('Alias')
    channel = relationship('Channel')
    processing_type1 = relationship('ProcessingType')
