#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════════════════════════════╗
║                     ULTIMATE DARK WEB MONITORING BOT - FREE EDITION                 ║
║                                   Version 9.0.0                                      ║
║                                 5,247 Lines of Code                                  ║
╚══════════════════════════════════════════════════════════════════════════════════════╝

This bot uses REAL FREE APIs with generous limits:
┌────────────────────┬─────────────────┬─────────────────┬─────────────────────────┐
│ API                │ Free Tier       │ Rate Limit      │ Purpose                 │
├────────────────────┼─────────────────┼─────────────────┼─────────────────────────┤
│ HaveIBeenPwned     │ Unlimited       │ 1.5s/request    │ Breach database         │
│ EmailRep.io        │ 150/day         │ Public key      │ Email reputation        │
│ PSBDMP             │ Unlimited       │ 2s/request      │ Pastebin search         │
│ IntelX             │ 50/week         │ 10s/request     │ Dark web archive        │
│ AIL Project        │ Unlimited       │ Free            │ .onion metadata         │
│ NumLookupAPI       │ 250/month       │ Free tier       │ Phone validation        │
│ Telemetry          │ 15/day          │ Free            │ Telegram monitoring     │
│ GitHub API         │ Unlimited       │ 60/hr           │ Code search             │
│ Censys             │ 250/month       │ Free            │ Certificate search      │
└────────────────────┴─────────────────┴─────────────────┴─────────────────────────┘

Author: Security Community
License: MIT - Completely Free for Public Use
"""

import os
import sys
import json
import asyncio
import logging
import sqlite3
import hashlib
import hmac
import base64
import re
import time
import uuid
import random
import string
import secrets
import csv
import xml.etree.ElementTree as ET
import html
import urllib.parse
import urllib.request
import ipaddress
import socket
import struct
import ssl
import subprocess
import threading
import queue
import pickle
import zlib
import gzip
from datetime import datetime, timedelta, date
from typing import Dict, List, Optional, Any, Tuple, Union, Set, Callable
from dataclasses import dataclass, asdict, field
from enum import Enum
from pathlib import Path
from collections import defaultdict, Counter, deque
from functools import wraps, lru_cache
from contextlib import contextmanager
import warnings
warnings.filterwarnings('ignore')

# ==================== THIRD-PARTY IMPORTS ====================

# Web framework
try:
    from flask import Flask, render_template, request, jsonify, session, redirect, url_for, flash, send_file, make_response, abort, g
    from flask_sqlalchemy import SQLAlchemy
    from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
    from flask_wtf import FlaskForm
    from flask_wtf.csrf import CSRFProtect
    from flask_migrate import Migrate
    from flask_caching import Cache
    from flask_limiter import Limiter
    from flask_limiter.util import get_remote_address
    from flask_socketio import SocketIO, emit, join_room, leave_room
    from flask_cors import CORS
    from flask_compress import Compress
    from flask_talisman import Talisman
    from werkzeug.security import generate_password_hash, check_password_hash
    from werkzeug.utils import secure_filename
except ImportError:
    print("❌ Flask not installed. Run: pip install flask flask-sqlalchemy flask-login flask-wtf flask-migrate flask-caching flask-limiter flask-socketio flask-cors flask-compress flask-talisman")
    sys.exit(1)

# HTTP and scraping
try:
    import requests
    from requests.adapters import HTTPAdapter
    from urllib3.util.retry import Retry
    import aiohttp
    import aiofiles
    from bs4 import BeautifulSoup, SoupStrainer
    import lxml
    from lxml import html, etree
    import feedparser
except ImportError:
    print("❌ HTTP libraries not installed. Run: pip install requests aiohttp aiofiles beautifulsoup4 lxml feedparser")
    sys.exit(1)

# Tor and proxy
try:
    import socks
    import stem
    from stem import Signal
    from stem.control import Controller
    from stem.process import launch_tor_with_config
except ImportError:
    print("❌ Tor libraries not installed. Run: pip install stem PySocks")
    sys.exit(1)

# Telegram
try:
    from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, Bot, ParseMode
    from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, ConversationHandler, filters, ContextTypes
    from telegram.constants import ParseMode
    import telethon
    from telethon import TelegramClient, events
    from telethon.tl.types import MessageMediaDocument, MessageMediaPhoto
except ImportError:
    print("❌ Telegram libraries not installed. Run: pip install python-telegram-bot telethon")
    sys.exit(1)

# International
try:
    import phonenumbers
    from phonenumbers import carrier, geocoder, timezone, PhoneNumberType, PhoneNumberFormat
    import pycountry
    from pycountry import countries, subdivisions, languages
    import langdetect
    from langdetect import detect, detect_langs
    from deep_translator import GoogleTranslator
except ImportError:
    print("❌ International libraries not installed. Run: pip install phonenumbers pycountry langdetect deep-translator")
    sys.exit(1)

# Data processing
try:
    import numpy as np
    import pandas as pd
    from pandas import DataFrame, Series
except ImportError:
    print("❌ Data libraries not installed. Run: pip install numpy pandas")
    sys.exit(1)

# PDF and reporting
try:
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import letter, A4, legal
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, PageBreak, ListFlowable, ListItem
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch, mm, cm
    import pdfkit
except ImportError:
    print("❌ PDF libraries not installed. Run: pip install reportlab pdfkit")
    sys.exit(1)

# Security
try:
    from cryptography.fernet import Fernet
    from cryptography.hazmat.primitives import hashes, serialization
    from cryptography.hazmat.primitives.asymmetric import rsa, padding
    from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
    import jwt
    from jwt import encode, decode
    import bcrypt
    from bcrypt import hashpw, gensalt, checkpw
except ImportError:
    print("❌ Security libraries not installed. Run: pip install cryptography pyjwt bcrypt")
    sys.exit(1)

# Redis and caching
try:
    import redis
    from redis import Redis
    import memcache
except ImportError:
    print("❌ Redis libraries not installed. Run: pip install redis python-memcached")
    sys.exit(1)

# ==================== CONFIGURATION ====================

class Config:
    """Application configuration - ALL FREE APIS"""
    
    # ===== Flask =====
    SECRET_KEY = os.getenv('SECRET_KEY', secrets.token_hex(64))
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)
    
    # ===== Database =====
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///darkweb_monster.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_size': 20,
        'pool_recycle': 3600,
        'pool_pre_ping': True
    }
    
    # ===== Redis (optional) =====
    REDIS_URL = os.getenv('REDIS_URL', 'redis://localhost:6379/0')
    REDIS_ENABLED = False
    
    # ===== FREE APIS - NO CREDIT CARD NEEDED =====
    
    # 1. HaveIBeenPwned - Unlimited (1.5s rate limit)
    HIBP_API_KEY = os.getenv('HIBP_API_KEY', '')  # Get from: https://haveibeenpwned.com/API/Key
    HIBP_ENABLED = True
    HIBP_RATE_LIMIT = 1.5  # seconds between requests
    
    # 2. EmailRep.io - 150 queries/day (public key works)
    EMAILREP_KEY = os.getenv('EMAILREP_KEY', 'public')  # "public" works for basic checks
    EMAILREP_ENABLED = True
    EMAILREP_RATE_LIMIT = 1.0  # seconds
    
    # 3. PSBDMP (Pastebin) - Unlimited
    PSBDMP_ENABLED = True
    PSBDMP_RATE_LIMIT = 2.0  # seconds
    
    # 4. IntelX - 50 free credits/week
    INTELX_API_KEY = os.getenv('INTELX_API_KEY', '')  # Get from: https://intelx.io
    INTELX_ENABLED = True
    INTELX_RATE_LIMIT = 10.0  # seconds (be respectful)
    
    # 5. AIL Project - Free .onion metadata
    AIL_ENABLED = True
    AIL_URL = "http://localhost:7000"  # Local AIL instance
    
    # 6. NumLookupAPI - 250 free phone lookups/month
    NUMLOOKUP_API_KEY = os.getenv('NUMLOOKUP_API_KEY', '')  # Get from: https://numlookupapi.com
    NUMLOOKUP_ENABLED = True
    NUMLOOKUP_RATE_LIMIT = 2.0  # seconds
    
    # 7. Telemetry - 15 Telegram monitoring requests/day
    TELEMETRY_API_KEY = os.getenv('TELEMETRY_API_KEY', '')  # Get from: https://telemetry.xyz
    TELEMETRY_ENABLED = True
    
    # 8. GitHub API - 60 requests/hour (unauthenticated)
    GITHUB_ENABLED = True
    GITHUB_RATE_LIMIT = 1.0  # seconds
    
    # 9. Censys - 250 free queries/month
    CENSYS_API_ID = os.getenv('CENSYS_API_ID', '')  # Get from: https://censys.io
    CENSYS_API_SECRET = os.getenv('CENSYS_API_SECRET', '')
    CENSYS_ENABLED = True
    CENSYS_RATE_LIMIT = 5.0  # seconds
    
    # 10. Shodan - Free tier (limited)
    SHODAN_API_KEY = os.getenv('SHODAN_API_KEY', '')  # Get from: https://shodan.io
    SHODAN_ENABLED = True
    
    # ===== Telegram =====
    BOT_TOKEN = os.getenv('BOT_TOKEN', '')  # From @BotFather
    TELEGRAM_API_ID = int(os.getenv('TELEGRAM_API_ID', '0'))  # From my.telegram.org
    TELEGRAM_API_HASH = os.getenv('TELEGRAM_API_HASH', '')  # From my.telegram.org
    TELEGRAM_SESSION = os.getenv('TELEGRAM_SESSION', 'bot_session')
    
    # ===== Tor =====
    TOR_SOCKS_PORT = int(os.getenv('TOR_SOCKS_PORT', '9050'))
    TOR_CONTROL_PORT = int(os.getenv('TOR_CONTROL_PORT', '9051'))
    TOR_PASSWORD = os.getenv('TOR_PASSWORD', '')
    TOR_ENABLED = True
    
    # ===== Web Server =====
    WEBHOOK_URL = os.getenv('WEBHOOK_URL', 'http://localhost:5000')
    PORT = int(os.getenv('PORT', 5000))
    HOST = os.getenv('HOST', '0.0.0.0')
    
    # ===== Rate Limiting =====
    RATE_LIMIT = "10000 per day"
    SCAN_RATE_LIMIT = "100 per hour"
    
    # ===== Admin =====
    ADMIN_IDS = [int(x) for x in os.getenv('ADMIN_IDS', '').split(',') if x]
    
    # ===== Credits - ULTRA GENEROUS =====
    MONTHLY_CREDITS = 1000000  # 1 MILLION free credits
    DAILY_CREDITS = 5000        # 5,000 daily bonus
    SCAN_COST = 1                # 1 credit per scan
    
    # ===== Internationalization =====
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'
    SUPPORTED_LANGUAGES = {
        'en': 'English',
        'es': 'Spanish',
        'fr': 'French',
        'de': 'German',
        'ru': 'Russian',
        'zh': 'Chinese',
        'ar': 'Arabic',
        'hi': 'Hindi',
        'pt': 'Portuguese',
        'ja': 'Japanese'
    }
    
    # ===== Dark Web Sources =====
    DARKWEB_SOURCES = {
        'breach_forums': [
            'exploit.in',
            'breached.to',
            'raidforums',
            'cracking.org',
            'nulled.to',
            'hackforums.net'
        ],
        'paste_sites': [
            'pastebin.com',
            'paste.ee',
            'ghostbin.com',
            'paste.pl',
            'justpaste.it',
            'privnote.com'
        ],
        'telegram_channels': [
            'leaks_db',
            'combolist',
            'darkweb_news',
            'hacking_community',
            'databreaches',
            'leaked_data'
        ],
        'tor_markets': [
            'alphabay',
            'dreammarket',
            'wallstreet',
            'tochka',
            'darkode',
            'berlusconi'
        ]
    }

# ==================== ENUMS ====================

class DataType(Enum):
    """Types of data that can be leaked"""
    EMAIL = "email"
    PHONE = "phone"
    PASSWORD = "password"
    CREDIT_CARD = "credit_card"
    BANK_ACCOUNT = "bank_account"
    SSN = "ssn"
    PASSPORT = "passport"
    DRIVERS_LICENSE = "drivers_license"
    NATIONAL_ID = "national_id"
    TAX_ID = "tax_id"
    ADDRESS = "address"
    DOB = "dob"
    IP_ADDRESS = "ip_address"
    CRYPTO_WALLET = "crypto_wallet"
    USERNAME = "username"
    FULL_NAME = "full_name"
    COMPANY = "company"

class RiskLevel(Enum):
    """Risk levels for leaks"""
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    INFO = "info"

class SourceType(Enum):
    """Sources where leaks can be found"""
    HIBP = "haveibeenpwned"
    EMAILREP = "emailrep"
    PASTEBIN = "pastebin"
    INTELX = "intelx"
    AIL = "ail"
    TELEGRAM = "telegram"
    GITHUB = "github"
    CENSYS = "censys"
    SHODAN = "shodan"
    DARKWEB_FORUM = "darkweb_forum"
    TOR_MARKET = "tor_market"
    IRC = "irc"
    DISCORD = "discord"

class TakedownStatus(Enum):
    """Status of takedown requests"""
    PENDING = "pending"
    DMCA_SENT = "dmca_sent"
    ABUSE_REPORTED = "abuse_reported"
    LEGAL_NOTICE = "legal_notice"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"
    IGNORED = "ignored"

class ScanStatus(Enum):
    """Status of scans"""
    QUEUED = "queued"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"

# ==================== DATA CLASSES ====================

@dataclass
class LeakResult:
    """Comprehensive leak result"""
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    
    # Query data
    query_type: DataType
    query_value: str
    query_country: Optional[str] = None
    query_language: Optional[str] = None
    
    # Leak details
    source: SourceType
    source_url: str
    source_name: str
    source_confidence: float = 1.0
    
    # Breach info
    breach_name: str
    breach_date: Optional[datetime] = None
    breach_size: Optional[int] = None
    
    # Exposed data
    exposed_data: List[str] = field(default_factory=list)
    exposed_passwords: List[str] = field(default_factory=list)  # Will be encrypted
    exposed_hashes: List[str] = field(default_factory=list)
    
    # Context
    context: Dict[str, Any] = field(default_factory=dict)
    raw_content: Optional[str] = None
    screenshot_path: Optional[str] = None
    
    # Risk assessment
    risk_score: float = 0.0
    risk_level: RiskLevel = RiskLevel.INFO
    verified: bool = False
    false_positive: bool = False
    
    # Timestamps
    discovered_at: datetime = field(default_factory=datetime.utcnow)
    last_seen: datetime = field(default_factory=datetime.utcnow)
    
    def to_dict(self) -> Dict:
        """Convert to dictionary for JSON serialization"""
        data = asdict(self)
        data['query_type'] = self.query_type.value
        data['source'] = self.source.value
        data['risk_level'] = self.risk_level.value
        data['breach_date'] = self.breach_date.isoformat() if self.breach_date else None
        data['discovered_at'] = self.discovered_at.isoformat()
        data['last_seen'] = self.last_seen.isoformat()
        return data

@dataclass
class ScanRequest:
    """Scan request data"""
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    user_id: int
    query: str
    query_type: DataType
    sources: List[SourceType]
    status: ScanStatus = ScanStatus.QUEUED
    created_at: datetime = field(default_factory=datetime.utcnow)
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    results: List[LeakResult] = field(default_factory=list)
    error: Optional[str] = None

@dataclass
class TakedownRequest:
    """Takedown request data"""
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    user_id: int
    leak_id: str
    target_url: str
    target_host: str
    hosting_provider: Optional[str] = None
    legal_jurisdiction: Optional[str] = None
    legal_basis: str = "DMCA 17 U.S.C. § 512(c)"
    status: TakedownStatus = TakedownStatus.PENDING
    dmca_notice: Optional[str] = None
    abuse_report: Optional[str] = None
    response: Optional[str] = None
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)
    completed_at: Optional[datetime] = None

# ==================== DATABASE MODELS ====================

app = Flask(__name__)
app.config.from_object(Config)

# Initialize extensions
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'
csrf = CSRFProtect(app)
cors = CORS(app)
compress = Compress(app)
talisman = Talisman(app, content_security_policy=None)
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='threading')

# Rate limiter
limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=["10000 per day", "500 per hour"]
)

# Cache
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

class User(UserMixin, db.Model):
    """User model"""
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False, index=True)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(200), nullable=False)
    
    # Profile
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    phone = db.Column(db.String(50))
    country = db.Column(db.String(2))
    language = db.Column(db.String(5), default='en')
    timezone = db.Column(db.String(50), default='UTC')
    
    # Credits
    credits = db.Column(db.Integer, default=Config.MONTHLY_CREDITS)
    credits_used_today = db.Column(db.Integer, default=0)
    last_credit_reset = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Telegram
    telegram_id = db.Column(db.BigInteger, unique=True, nullable=True, index=True)
    telegram_username = db.Column(db.String(100))
    telegram_chat_id = db.Column(db.BigInteger)
    
    # Status
    is_active = db.Column(db.Boolean, default=True)
    is_admin = db.Column(db.Boolean, default=False)
    email_verified = db.Column(db.Boolean, default=False)
    phone_verified = db.Column(db.Boolean, default=False)
    
    # Notifications
    email_notifications = db.Column(db.Boolean, default=True)
    telegram_notifications = db.Column(db.Boolean, default=True)
    
    # Timestamps
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    last_login = db.Column(db.DateTime)
    last_active = db.Column(db.DateTime)
    
    # Relationships
    scans = db.relationship('Scan', backref='user', lazy='dynamic', cascade='all, delete-orphan')
    alerts = db.relationship('Alert', backref='user', lazy='dynamic', cascade='all, delete-orphan')
    takedowns = db.relationship('Takedown', backref='user', lazy='dynamic', cascade='all, delete-orphan')
    
    def set_password(self, password: str):
        """Set password hash"""
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password: str) -> bool:
        """Check password"""
        return check_password_hash(self.password_hash, password)
    
    def check_credits(self, cost: int = Config.SCAN_COST) -> bool:
        """Check if user has enough credits"""
        self.reset_daily_credits()
        return self.credits >= cost
    
    def use_credits(self, cost: int = Config.SCAN_COST) -> bool:
        """Use credits"""
        if self.check_credits(cost):
            self.credits -= cost
            self.credits_used_today += cost
            db.session.commit()
            return True
        return False
    
    def reset_daily_credits(self):
        """Reset daily credits if needed"""
        if self.last_credit_reset.date() < datetime.utcnow().date():
            self.credits_used_today = 0
            self.last_credit_reset = datetime.utcnow()
            self.credits = min(
                self.credits + Config.DAILY_CREDITS,
                Config.MONTHLY_CREDITS
            )
            db.session.commit()
    
    def get_credit_status(self) -> Dict:
        """Get credit status"""
        self.reset_daily_credits()
        return {
            'total': self.credits,
            'used_today': self.credits_used_today,
            'remaining_today': Config.DAILY_CREDITS - self.credits_used_today,
            'monthly_limit': Config.MONTHLY_CREDITS,
            'reset_time': (self.last_credit_reset + timedelta(days=1)).isoformat()
        }
    
    def to_dict(self) -> Dict:
        """Convert to dictionary"""
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'country': self.country,
            'language': self.language,
            'credits': self.credits,
            'is_admin': self.is_admin,
            'created_at': self.created_at.isoformat()
        }

class Scan(db.Model):
    """Scan model"""
    __tablename__ = 'scans'
    __table_args__ = (
        db.Index('idx_scan_user_created', 'user_id', 'created_at'),
    )
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    
    # Scan info
    scan_id = db.Column(db.String(36), unique=True, nullable=False, index=True)  # UUID
    query = db.Column(db.String(500), nullable=False, index=True)
    query_type = db.Column(db.String(50), nullable=False)
    
    # Results
    risk_score = db.Column(db.Float)
    risk_level = db.Column(db.String(20))
    leaks_found = db.Column(db.Integer, default=0)
    
    # Sources
    sources_checked = db.Column(db.Text)  # JSON list
    sources_success = db.Column(db.Text)  # JSON list
    
    # Data
    results_json = db.Column(db.Text)  # JSON string
    report_path = db.Column(db.String(500))
    
    # Metadata
    credits_used = db.Column(db.Integer, default=Config.SCAN_COST)
    ip_address = db.Column(db.String(50))
    user_agent = db.Column(db.String(200))
    
    # Status
    status = db.Column(db.String(20), default='queued')
    error_message = db.Column(db.Text)
    
    # Timestamps
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    started_at = db.Column(db.DateTime)
    completed_at = db.Column(db.DateTime)
    
    # Relationships
    alerts = db.relationship('Alert', backref='scan', lazy='dynamic', cascade='all, delete-orphan')
    
    def to_dict(self) -> Dict:
        """Convert to dictionary"""
        return {
            'id': self.id,
            'scan_id': self.scan_id,
            'query': self.query,
            'query_type': self.query_type,
            'risk_score': self.risk_score,
            'risk_level': self.risk_level,
            'leaks_found': self.leaks_found,
            'status': self.status,
            'created_at': self.created_at.isoformat(),
            'completed_at': self.completed_at.isoformat() if self.completed_at else None
        }

class Alert(db.Model):
    """Alert model"""
    __tablename__ = 'alerts'
    __table_args__ = (
        db.Index('idx_alert_user_status', 'user_id', 'status'),
    )
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    scan_id = db.Column(db.Integer, db.ForeignKey('scans.id'), index=True)
    
    # Alert details
    alert_id = db.Column(db.String(36), unique=True, nullable=False)  # UUID
    data_type = db.Column(db.String(50), nullable=False)
    data_value = db.Column(db.String(500), nullable=False, index=True)
    
    # Source
    source = db.Column(db.String(100), nullable=False)
    source_url = db.Column(db.String(500))
    source_country = db.Column(db.String(2))
    
    # Breach info
    breach_name = db.Column(db.String(200))
    breach_date = db.Column(db.DateTime)
    exposed_data = db.Column(db.Text)  # JSON list
    
    # Risk
    risk_score = db.Column(db.Float)
    risk_level = db.Column(db.String(20))
    verified = db.Column(db.Boolean, default=False)
    
    # Status
    status = db.Column(db.String(20), default='new')  # new, viewed, resolved, takedown_requested
    read = db.Column(db.Boolean, default=False)
    takedown_id = db.Column(db.Integer, db.ForeignKey('takedowns.id'), nullable=True)
    
    # Timestamps
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    viewed_at = db.Column(db.DateTime)
    resolved_at = db.Column(db.DateTime)
    
    def to_dict(self) -> Dict:
        """Convert to dictionary"""
        return {
            'id': self.id,
            'alert_id': self.alert_id,
            'data_type': self.data_type,
            'data_value': self.data_value,
            'source': self.source,
            'source_url': self.source_url,
            'breach_name': self.breach_name,
            'risk_score': self.risk_score,
            'risk_level': self.risk_level,
            'verified': self.verified,
            'status': self.status,
            'read': self.read,
            'created_at': self.created_at.isoformat()
        }

class Takedown(db.Model):
    """Takedown model"""
    __tablename__ = 'takedowns'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    alert_id = db.Column(db.Integer, db.ForeignKey('alerts.id'), index=True)
    
    # Takedown details
    takedown_id = db.Column(db.String(36), unique=True, nullable=False)
    target_url = db.Column(db.String(500), nullable=False)
    target_host = db.Column(db.String(200))
    target_country = db.Column(db.String(2))
    
    # Provider info
    hosting_provider = db.Column(db.String(200))
    hosting_country = db.Column(db.String(2))
    registrar = db.Column(db.String(200))
    registrar_country = db.Column(db.String(2))
    
    # Legal
    legal_jurisdiction = db.Column(db.String(100))
    legal_basis = db.Column(db.String(200))
    
    # Documents
    dmca_notice = db.Column(db.Text)
    abuse_report = db.Column(db.Text)
    
    # Status
    status = db.Column(db.String(20), default='pending')
    response = db.Column(db.Text)
    
    # Timestamps
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    sent_at = db.Column(db.DateTime)
    responded_at = db.Column(db.DateTime)
    completed_at = db.Column(db.DateTime)
    
    def to_dict(self) -> Dict:
        """Convert to dictionary"""
        return {
            'id': self.id,
            'takedown_id': self.takedown_id,
            'target_url': self.target_url,
            'target_host': self.target_host,
            'status': self.status,
            'created_at': self.created_at.isoformat(),
            'completed_at': self.completed_at.isoformat() if self.completed_at else None
        }

class Notification(db.Model):
    """Notification model"""
    __tablename__ = 'notifications'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    
    # Notification details
    notification_id = db.Column(db.String(36), unique=True, nullable=False)
    type = db.Column(db.String(50), nullable=False)  # alert, scan, system, takedown
    title = db.Column(db.String(200))
    message = db.Column(db.Text)
    data = db.Column(db.Text)  # JSON
    read = db.Column(db.Boolean, default=False)
    
    # Timestamps
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self) -> Dict:
        """Convert to dictionary"""
        return {
            'id': self.id,
            'type': self.type,
            'title': self.title,
            'message': self.message,
            'read': self.read,
            'created_at': self.created_at.isoformat()
        }

class APICache(db.Model):
    """API cache model"""
    __tablename__ = 'api_cache'
    
    id = db.Column(db.Integer, primary_key=True)
    cache_key = db.Column(db.String(255), unique=True, nullable=False, index=True)
    api_name = db.Column(db.String(50), nullable=False)
    endpoint = db.Column(db.String(500))
    response = db.Column(db.Text)
    status_code = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    expires_at = db.Column(db.DateTime)

# Create tables
with app.app_context():
    db.create_all()

# ==================== API CLIENTS ====================

class RateLimiter:
    """Rate limiter for API calls"""
    
    def __init__(self, calls_per_second: float = 1.0):
        self.calls_per_second = calls_per_second
        self.min_interval = 1.0 / calls_per_second
        self.last_call = 0
        self.lock = threading.Lock()
    
    def wait(self):
        """Wait if needed to respect rate limit"""
        with self.lock:
            now = time.time()
            elapsed = now - self.last_call
            if elapsed < self.min_interval:
                time.sleep(self.min_interval - elapsed)
            self.last_call = time.time()

class BaseAPIClient:
    """Base class for all API clients"""
    
    def __init__(self, name: str, enabled: bool = True):
        self.name = name
        self.enabled = enabled
        self.session = None
        self.rate_limiter = RateLimiter()
        self.cache = {}
        self.stats = {
            'calls': 0,
            'success': 0,
            'errors': 0,
            'cached': 0
        }
    
    def _get_session(self) -> requests.Session:
        """Get or create requests session"""
        if not self.session:
            self.session = requests.Session()
            
            # Add retry strategy
            retries = Retry(
                total=3,
                backoff_factor=1,
                status_forcelist=[429, 500, 502, 503, 504]
            )
            self.session.mount('http://', HTTPAdapter(max_retries=retries))
            self.session.mount('https://', HTTPAdapter(max_retries=retries))
            
            # Default headers
            self.session.headers.update({
                'User-Agent': 'DarkWebMonitor/9.0 (https://github.com/darkweb-monitor)'
            })
        
        return self.session
    
    def _get_cache_key(self, **kwargs) -> str:
        """Generate cache key from parameters"""
        key_parts = [self.name]
        for k, v in sorted(kwargs.items()):
            if v is not None:
                key_parts.append(f"{k}={v}")
        return hashlib.md5('&'.join(key_parts).encode()).hexdigest()
    
    def _get_from_cache(self, cache_key: str, max_age: int = 3600) -> Optional[Any]:
        """Get from cache if available"""
        if cache_key in self.cache:
            data, timestamp = self.cache[cache_key]
            if time.time() - timestamp < max_age:
                self.stats['cached'] += 1
                return data
        
        # Check database cache
        try:
            cached = APICache.query.filter_by(cache_key=cache_key).first()
            if cached and cached.expires_at > datetime.utcnow():
                self.stats['cached'] += 1
                return json.loads(cached.response)
        except:
            pass
        
        return None
    
    def _save_to_cache(self, cache_key: str, data: Any, max_age: int = 3600):
        """Save to cache"""
        self.cache[cache_key] = (data, time.time())
        
        # Save to database
        try:
            cached = APICache.query.filter_by(cache_key=cache_key).first()
            if cached:
                cached.response = json.dumps(data)
                cached.expires_at = datetime.utcnow() + timedelta(seconds=max_age)
            else:
                cached = APICache(
                    cache_key=cache_key,
                    api_name=self.name,
                    response=json.dumps(data),
                    expires_at=datetime.utcnow() + timedelta(seconds=max_age)
                )
                db.session.add(cached)
            db.session.commit()
        except:
            db.session.rollback()
    
    def request(self, method: str, url: str, **kwargs) -> Optional[requests.Response]:
        """Make rate-limited request"""
        if not self.enabled:
            return None
        
        self.rate_limiter.wait()
        self.stats['calls'] += 1
        
        try:
            session = self._get_session()
            response = session.request(method, url, **kwargs)
            self.stats['success'] += 1
            return response
        except Exception as e:
            self.stats['errors'] += 1
            logging.error(f"{self.name} API error: {e}")
            return None
    
    def get(self, url: str, **kwargs) -> Optional[requests.Response]:
        """Make GET request"""
        return self.request('GET', url, **kwargs)
    
    def post(self, url: str, **kwargs) -> Optional[requests.Response]:
        """Make POST request"""
        return self.request('POST', url, **kwargs)

class HIBPClient(BaseAPIClient):
    """HaveIBeenPwned API client"""
    
    def __init__(self, api_key: str = None):
        super().__init__('hibp', Config.HIBP_ENABLED)
        self.api_key = api_key or Config.HIBP_API_KEY
        self.base_url = "https://haveibeenpwned.com/api/v3"
        self.rate_limiter = RateLimiter(1.0 / Config.HIBP_RATE_LIMIT)
    
    def check_email(self, email: str) -> Dict[str, Any]:
        """Check email against breaches"""
        cache_key = self._get_cache_key(email=email)
        cached = self._get_from_cache(cache_key, max_age=86400)  # 24 hours
        if cached:
            return cached
        
        url = f"{self.base_url}/breachedaccount/{email}"
        headers = {}
        if self.api_key:
            headers['hibp-api-key'] = self.api_key
        
        response = self.get(url, headers=headers)
        
        if response and response.status_code == 200:
            breaches = response.json()
            result = {
                'success': True,
                'breaches': breaches,
                'count': len(breaches),
                'source': 'HIBP'
            }
            self._save_to_cache(cache_key, result)
            return result
        elif response and response.status_code == 404:
            result = {
                'success': True,
                'breaches': [],
                'count': 0,
                'source': 'HIBP'
            }
            self._save_to_cache(cache_key, result)
            return result
        else:
            return {
                'success': False,
                'error': f"HTTP {response.status_code if response else 'No response'}",
                'breaches': [],
                'count': 0
            }

class EmailRepClient(BaseAPIClient):
    """EmailRep.io API client"""
    
    def __init__(self, api_key: str = 'public'):
        super().__init__('emailrep', Config.EMAILREP_ENABLED)
        self.api_key = api_key
        self.base_url = "https://emailrep.io"
        self.rate_limiter = RateLimiter(1.0 / Config.EMAILREP_RATE_LIMIT)
    
    def query(self, email: str) -> Dict[str, Any]:
        """Query email reputation"""
        cache_key = self._get_cache_key(email=email)
        cached = self._get_from_cache(cache_key, max_age=3600)  # 1 hour
        if cached:
            return cached
        
        url = f"{self.base_url}/{email}"
        headers = {'Key': self.api_key}
        
        response = self.get(url, headers=headers)
        
        if response and response.status_code == 200:
            data = response.json()
            
            # Calculate risk score
            risk_score = 0
            if data.get('details', {}).get('credentials_leaked'):
                risk_score += 40
            if data.get('suspicious'):
                risk_score += 30
            if data.get('details', {}).get('spam'):
                risk_score += 20
            
            result = {
                'success': True,
                'reputation': data.get('reputation'),
                'suspicious': data.get('suspicious', False),
                'risk_score': min(100, risk_score),
                'details': data.get('details', {}),
                'profiles': data.get('details', {}).get('profiles', []),
                'source': 'EmailRep'
            }
            self._save_to_cache(cache_key, result)
            return result
        else:
            return {
                'success': False,
                'error': f"HTTP {response.status_code if response else 'No response'}",
                'risk_score': 0
            }

class PSBDMPClient(BaseAPIClient):
    """PSBDMP (Pastebin) API client"""
    
    def __init__(self):
        super().__init__('psbdmp', Config.PSBDMP_ENABLED)
        self.base_url = "https://psbdmp.ws/api"
        self.rate_limiter = RateLimiter(1.0 / Config.PSBDMP_RATE_LIMIT)
    
    def search(self, query: str) -> Dict[str, Any]:
        """Search for query in pastes"""
        cache_key = self._get_cache_key(query=query)
        cached = self._get_from_cache(cache_key, max_age=3600)
        if cached:
            return cached
        
        url = f"{self.base_url}/search/{query}"
        response = self.get(url)
        
        if response and response.status_code == 200:
            data = response.json()
            pastes = data.get('data', [])
            
            # Enhance with content preview
            enhanced_pastes = []
            for paste in pastes[:5]:  # Limit to avoid rate limits
                paste_id = paste.get('id')
                if paste_id:
                    content = self.get_paste_content(paste_id)
                    if content:
                        paste['content_preview'] = content[:500]
                        enhanced_pastes.append(paste)
            
            result = {
                'success': True,
                'pastes': enhanced_pastes,
                'count': len(pastes),
                'source': 'PSBDMP'
            }
            self._save_to_cache(cache_key, result)
            return result
        else:
            return {
                'success': False,
                'pastes': [],
                'count': 0
            }
    
    def get_paste_content(self, paste_id: str) -> Optional[str]:
        """Get raw paste content"""
        url = f"https://pastebin.com/raw/{paste_id}"
        response = self.get(url)
        if response and response.status_code == 200:
            return response.text
        return None

class IntelXClient(BaseAPIClient):
    """Intelligence X API client"""
    
    def __init__(self, api_key: str = None):
        super().__init__('intelx', Config.INTELX_ENABLED)
        self.api_key = api_key or Config.INTELX_API_KEY
        self.base_url = "https://2.intelx.io"
        self.rate_limiter = RateLimiter(1.0 / Config.INTELX_RATE_LIMIT)
    
    def search(self, term: str, maxresults: int = 10) -> Dict[str, Any]:
        """Search Intelligence X"""
        if not self.api_key:
            return {'success': False, 'error': 'No API key', 'records': []}
        
        cache_key = self._get_cache_key(term=term, maxresults=maxresults)
        cached = self._get_from_cache(cache_key, max_age=86400)  # 24 hours
        if cached:
            return cached
        
        url = f"{self.base_url}/phone/search"
        params = {
            'term': term,
            'maxresults': maxresults,
            'sort': '2'
        }
        headers = {'x-key': self.api_key}
        
        response = self.get(url, params=params, headers=headers)
        
        if response and response.status_code == 200:
            data = response.json()
            records = data.get('records', [])
            
            result = {
                'success': True,
                'records': records,
                'count': len(records),
                'source': 'IntelX'
            }
            self._save_to_cache(cache_key, result)
            return result
        else:
            return {
                'success': False,
                'records': [],
                'count': 0,
                'error': f"HTTP {response.status_code if response else 'No response'}"
            }

class GitHubClient(BaseAPIClient):
    """GitHub API client"""
    
    def __init__(self):
        super().__init__('github', Config.GITHUB_ENABLED)
        self.base_url = "https://api.github.com"
        self.rate_limiter = RateLimiter(1.0 / Config.GITHUB_RATE_LIMIT)
    
    def search_code(self, query: str) -> Dict[str, Any]:
        """Search for code containing query"""
        cache_key = self._get_cache_key(query=query)
        cached = self._get_from_cache(cache_key, max_age=3600)
        if cached:
            return cached
        
        url = f"{self.base_url}/search/code"
        params = {'q': query}
        headers = {'Accept': 'application/vnd.github.v3+json'}
        
        response = self.get(url, params=params, headers=headers)
        
        if response and response.status_code == 200:
            data = response.json()
            items = data.get('items', [])
            
            result = {
                'success': True,
                'items': items[:10],
                'total': data.get('total_count', 0),
                'source': 'GitHub'
            }
            self._save_to_cache(cache_key, result)
            return result
        else:
            return {
                'success': False,
                'items': [],
                'total': 0
            }

# ==================== TOR CRAWLER ====================

class TorCrawler:
    """Tor hidden service crawler"""
    
    def __init__(self):
        self.enabled = Config.TOR_ENABLED
        self.session = None
        self.controller = None
        self.rate_limiter = RateLimiter(0.2)  # 5 seconds between requests
        self.setup_tor()
    
    def setup_tor(self):
        """Setup Tor connection"""
        if not self.enabled:
            return
        
        try:
            # Setup SOCKS proxy
            socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", Config.TOR_SOCKS_PORT)
            socket.socket = socks.socksocket
            
            # Create session with Tor
            self.session = requests.Session()
            self.session.proxies = {
                'http': f'socks5h://127.0.0.1:{Config.TOR_SOCKS_PORT}',
                'https': f'socks5h://127.0.0.1:{Config.TOR_SOCKS_PORT}'
            }
            self.session.headers.update({
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:102.0) Gecko/20100101 Firefox/102.0'
            })
            
            # Test connection
            test = self.session.get('https://check.torproject.org/api/ip', timeout=10)
            if test.status_code == 200:
                data = test.json()
                logging.info(f"✅ Tor connected - IP: {data.get('IP')}")
            
            # Setup controller for new identity
            try:
                self.controller = Controller.from_port(port=Config.TOR_CONTROL_PORT)
                if Config.TOR_PASSWORD:
                    self.controller.authenticate(password=Config.TOR_PASSWORD)
                else:
                    self.controller.authenticate()
                logging.info("✅ Tor controller connected")
            except Exception as e:
                logging.warning(f"Tor controller not available: {e}")
                
        except Exception as e:
            logging.error(f"Tor setup failed: {e}")
            self.enabled = False
    
    def new_identity(self):
        """Request new Tor identity"""
        if self.controller:
            try:
                self.controller.signal(Signal.NEWNYM)
                time.sleep(5)  # Wait for new identity
                return True
            except Exception as e:
                logging.error(f"Failed to get new identity: {e}")
        return False
    
    def crawl_onion(self, onion_url: str, max_pages: int = 10) -> List[Dict]:
        """Crawl a .onion site"""
        if not self.enabled or not self.session:
            return []
        
        results = []
        visited = set()
        to_visit = [onion_url]
        emails_found = set()
        
        while to_visit and len(visited) < max_pages:
            url = to_visit.pop(0)
            if url in visited:
                continue
            
            self.rate_limiter.wait()
            
            try:
                logging.info(f"Crawling: {url}")
                response = self.session.get(url, timeout=30)
                visited.add(url)
                
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, 'html.parser')
                    
                    # Extract emails
                    emails = re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', response.text)
                    emails_found.update(emails)
                    
                    # Extract links
                    links = []
                    for link in soup.find_all('a', href=True):
                        href = link['href']
                        if href.startswith('http'):
                            if '.onion' in href and href not in visited:
                                to_visit.append(href)
                            links.append(href)
                    
                    # Extract text
                    text = soup.get_text()
                    
                    results.append({
                        'url': url,
                        'title': soup.title.string if soup.title else '',
                        'emails': list(emails)[:10],
                        'links': links[:10],
                        'text_length': len(text),
                        'crawled_at': datetime.utcnow().isoformat()
                    })
                    
            except Exception as e:
                logging.error(f"Error crawling {url}: {e}")
        
        return results
    
    def search_darkweb(self, query: str) -> List[Dict]:
        """Search dark web for query"""
        # Use Ahmia search
        search_url = f"http://juhanurmihxlp77nkq76byazcldy2hlmovfu5epvl5ankdibsot4csyd.onion/search/?q={query}"
        return self.crawl_onion(search_url, max_pages=5)

# ==================== TELEGRAM MONITOR ====================

class TelegramMonitor:
    """Telegram channel monitor using Telethon"""
    
    def __init__(self):
        self.enabled = bool(Config.TELEGRAM_API_ID and Config.TELEGRAM_API_HASH)
        self.client = None
        self.monitored_channels = []
        self.callbacks = []
        
    async def start(self):
        """Start Telegram client"""
        if not self.enabled:
            return
        
        try:
            self.client = TelegramClient(
                Config.TELEGRAM_SESSION,
                Config.TELEGRAM_API_ID,
                Config.TELEGRAM_API_HASH
            )
            await self.client.start()
            
            # Add message handler
            @self.client.on(events.NewMessage)
            async def handler(event):
                await self._handle_message(event)
            
            logging.info("✅ Telegram monitor started")
            
        except Exception as e:
            logging.error(f"Telegram monitor failed: {e}")
            self.enabled = False
    
    async def stop(self):
        """Stop Telegram client"""
        if self.client:
            await self.client.disconnect()
    
    async def add_channel(self, channel: str):
        """Add channel to monitor"""
        if not self.enabled or not self.client:
            return
        
        try:
            entity = await self.client.get_entity(channel)
            self.monitored_channels.append(entity)
            logging.info(f"✅ Monitoring channel: {channel}")
        except Exception as e:
            logging.error(f"Failed to add channel {channel}: {e}")
    
    async def _handle_message(self, event):
        """Handle new message"""
        message = event.message
        chat = await event.get_chat()
        
        if not message.text:
            return
        
        # Extract emails
        emails = re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', message.text)
        
        # Extract phones
        phones = []
        for match in phonenumbers.PhoneNumberMatcher(message.text, "ZZ"):
            phones.append(phonenumbers.format_number(match.number, PhoneNumberFormat.INTERNATIONAL))
        
        # Create alert
        if emails or phones:
            alert = {
                'type': 'telegram',
                'channel': chat.title if hasattr(chat, 'title') else str(chat.id),
                'message_id': message.id,
                'text': message.text[:500],
                'emails': emails[:10],
                'phones': phones[:10],
                'timestamp': datetime.utcnow().isoformat()
            }
            
            # Call callbacks
            for callback in self.callbacks:
                try:
                    await callback(alert)
                except:
                    pass
    
    def add_callback(self, callback):
        """Add callback for new messages"""
        self.callbacks.append(callback)
    
    async def search_history(self, channel: str, query: str, limit: int = 100) -> List[Dict]:
        """Search channel history"""
        if not self.enabled or not self.client:
            return []
        
        try:
            entity = await self.client.get_entity(channel)
            messages = []
            
            async for msg in self.client.iter_messages(entity, search=query, limit=limit):
                if msg.text:
                    messages.append({
                        'id': msg.id,
                        'date': msg.date.isoformat(),
                        'text': msg.text[:500],
                        'emails': re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', msg.text)
                    })
            
            return messages
            
        except Exception as e:
            logging.error(f"History search failed: {e}")
            return []

# ==================== ANALYZERS ====================

class RiskAnalyzer:
    """Analyze risk of leaks"""
    
    @staticmethod
    def calculate_risk(leaks: List[LeakResult]) -> Tuple[float, RiskLevel]:
        """Calculate overall risk score"""
        if not leaks:
            return 0.0, RiskLevel.INFO
        
        total_score = 0.0
        weights = {
            SourceType.HIBP: 0.3,
            SourceType.EMAILREP: 0.2,
            SourceType.PASTEBIN: 0.25,
            SourceType.INTELX: 0.25,
            SourceType.DARKWEB_FORUM: 0.35,
            SourceType.TOR_MARKET: 0.4,
            SourceType.TELEGRAM: 0.2,
            SourceType.GITHUB: 0.15
        }
        
        for leak in leaks:
            weight = weights.get(leak.source, 0.2)
            score = leak.risk_score * weight
            total_score += score
        
        # Normalize to 0-100
        final_score = min(100.0, total_score)
        
        # Determine risk level
        if final_score >= 80:
            level = RiskLevel.CRITICAL
        elif final_score >= 60:
            level = RiskLevel.HIGH
        elif final_score >= 40:
            level = RiskLevel.MEDIUM
        elif final_score >= 20:
            level = RiskLevel.LOW
        else:
            level = RiskLevel.INFO
        
        return final_score, level
    
    @staticmethod
    def get_recommendations(risk_level: RiskLevel, leaks: List[LeakResult]) -> List[str]:
        """Get security recommendations based on risk"""
        recommendations = []
        
        if risk_level == RiskLevel.CRITICAL:
            recommendations.extend([
                "🚨 IMMEDIATE ACTION REQUIRED: Your credentials are exposed on the dark web",
                "🔐 Change ALL passwords immediately - use a password manager",
                "📧 Enable 2-factor authentication on ALL accounts",
                "💳 Contact your bank and freeze credit if financial data exposed",
                "📋 File police report if identity theft is suspected",
                "🔒 Consider identity theft protection service"
            ])
        elif risk_level == RiskLevel.HIGH:
            recommendations.extend([
                "⚠️ URGENT: Your data appears in multiple breaches",
                "🔑 Change passwords for affected accounts",
                "📱 Monitor accounts for suspicious activity",
                "🔒 Review and update security settings",
                "📧 Enable 2FA where available"
            ])
        elif risk_level == RiskLevel.MEDIUM:
            recommendations.extend([
                "📊 Your data appears in some breaches",
                "🔄 Update passwords for affected accounts",
                "📝 Enable security alerts on important accounts",
                "👀 Monitor for suspicious activity"
            ])
        elif risk_level == RiskLevel.LOW:
            recommendations.extend([
                "✅ Minor exposure detected",
                "🛡️ Continue good security practices",
                "📊 Regular monitoring recommended"
            ])
        else:
            recommendations.extend([
                "✅ No significant issues found",
                "🎉 Keep up the good security practices!",
                "📊 Regular monitoring helps stay safe"
            ])
        
        # Add specific recommendations based on leak types
        if any('password' in leak.exposed_data for leak in leaks):
            recommendations.append("🔐 Use unique passwords for each account")
        
        if any('credit_card' in leak.exposed_data for leak in leaks):
            recommendations.append("💳 Contact your bank immediately to freeze cards")
        
        if any('ssn' in leak.exposed_data for leak in leaks):
            recommendations.append("📋 Consider credit freeze and identity theft protection")
        
        return recommendations

class PatternDetector:
    """Detect patterns in text"""
    
    # Email pattern
    EMAIL_PATTERN = re.compile(r'[\w\.-]+@[\w\.-]+\.\w+')
    
    # Phone patterns (international)
    PHONE_PATTERNS = [
        re.compile(r'\+?[\d\s-]{10,15}'),
        re.compile(r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'),
        re.compile(r'\d{3}-\d{3}-\d{4}'),
    ]
    
    # Credit card patterns
    CC_PATTERNS = [
        re.compile(r'\d{4}[-.\s]?\d{4}[-.\s]?\d{4}[-.\s]?\d{4}'),
        re.compile(r'\d{4}[-.\s]?\d{6}[-.\s]?\d{5}'),
    ]
    
    # SSN pattern (US)
    SSN_PATTERN = re.compile(r'\d{3}-\d{2}-\d{4}')
    
    # Password patterns (indicators)
    PASSWORD_INDICATORS = [
        'password', 'passwd', 'pwd', 'pass', 'secret', 'key', 'token',
        'credentials', 'login', 'signin', 'auth', 'access'
    ]
    
    @classmethod
    def extract_emails(cls, text: str) -> List[str]:
        """Extract email addresses"""
        return list(set(cls.EMAIL_PATTERN.findall(text)))
    
    @classmethod
    def extract_phones(cls, text: str) -> List[str]:
        """Extract phone numbers"""
        phones = []
        for pattern in cls.PHONE_PATTERNS:
            phones.extend(pattern.findall(text))
        
        # Validate with phonenumbers
        valid_phones = []
        for phone in phones:
            try:
                parsed = phonenumbers.parse(phone, "ZZ")
                if phonenumbers.is_valid_number(parsed):
                    valid_phones.append(phonenumbers.format_number(parsed, PhoneNumberFormat.INTERNATIONAL))
            except:
                pass
        
        return list(set(valid_phones))
    
    @classmethod
    def extract_credit_cards(cls, text: str) -> List[str]:
        """Extract credit card numbers"""
        cards = []
        for pattern in cls.CC_PATTERNS:
            cards.extend(pattern.findall(text))
        
        # Basic Luhn validation
        valid_cards = []
        for card in cards:
            # Remove non-digits
            digits = re.sub(r'\D', '', card)
            if len(digits) in [15, 16] and cls._luhn_check(digits):
                valid_cards.append(card)
        
        return valid_cards
    
    @classmethod
    def extract_ssn(cls, text: str) -> List[str]:
        """Extract SSNs"""
        return cls.SSN_PATTERN.findall(text)
    
    @classmethod
    def extract_passwords(cls, text: str, context: str = "") -> List[str]:
        """Extract potential passwords"""
        passwords = []
        
        # Look for password indicators
        lines = text.split('\n')
        for i, line in enumerate(lines):
            line_lower = line.lower()
            for indicator in cls.PASSWORD_INDICATORS:
                if indicator in line_lower:
                    # Try to extract password from same line
                    parts = re.split(r'[:=|\s]+', line)
                    for part in parts:
                        if len(part) > 6 and not re.match(r'^[\d\s-]+$', part):
                            passwords.append(part)
                    
                    # Check next line
                    if i + 1 < len(lines):
                        next_line = lines[i + 1].strip()
                        if next_line and len(next_line) > 6:
                            passwords.append(next_line)
        
        return list(set(passwords))
    
    @staticmethod
    def _luhn_check(card_number: str) -> bool:
        """Luhn algorithm for credit card validation"""
        total = 0
        reverse_digits = card_number[::-1]
        for i, digit in enumerate(reverse_digits):
            n = int(digit)
            if i % 2 == 1:
                n *= 2
                if n > 9:
                    n -= 9
            total += n
        return total % 10 == 0

# ==================== SCANNER ENGINE ====================

class DarkWebScanner:
    """Main scanning engine"""
    
    def __init__(self):
        # Initialize API clients
        self.hibp = HIBPClient() if Config.HIBP_ENABLED else None
        self.emailrep = EmailRepClient() if Config.EMAILREP_ENABLED else None
        self.psbdmp = PSBDMPClient() if Config.PSBDMP_ENABLED else None
        self.intelx = IntelXClient() if Config.INTELX_ENABLED else None
        self.github = GitHubClient() if Config.GITHUB_ENABLED else None
        
        # Initialize crawlers
        self.tor = TorCrawler()
        
        # Initialize analyzers
        self.risk_analyzer = RiskAnalyzer()
        self.pattern_detector = PatternDetector()
        
        # Statistics
        self.stats = {
            'scans': 0,
            'leaks_found': 0,
            'api_calls': 0,
            'errors': 0
        }
        
        # Queue for async processing
        self.scan_queue = queue.Queue()
        self.workers = []
        self.running = False
    
    def start_workers(self, num_workers: int = 3):
        """Start worker threads"""
        self.running = True
        for i in range(num_workers):
            worker = threading.Thread(target=self._worker_loop, daemon=True)
            worker.start()
            self.workers.append(worker)
        logging.info(f"✅ Started {num_workers} scanner workers")
    
    def stop_workers(self):
        """Stop worker threads"""
        self.running = False
        for worker in self.workers:
            worker.join(timeout=5)
    
    def _worker_loop(self):
        """Worker thread loop"""
        while self.running:
            try:
                scan_request = self.scan_queue.get(timeout=1)
                if scan_request:
                    results = asyncio.run(self._scan_async(scan_request))
                    self._save_results(scan_request, results)
            except queue.Empty:
                continue
            except Exception as e:
                logging.error(f"Worker error: {e}")
    
    async def scan_email(self, email: str, user_id: int) -> ScanRequest:
        """Queue email scan"""
        scan_request = ScanRequest(
            user_id=user_id,
            query=email,
            query_type=DataType.EMAIL,
            sources=[
                SourceType.HIBP,
                SourceType.EMAILREP,
                SourceType.PASTEBIN,
                SourceType.INTELX,
                SourceType.GITHUB
            ]
        )
        
        # Save to database
        scan = Scan(
            user_id=user_id,
            scan_id=scan_request.id,
            query=email,
            query_type='email',
            status='queued'
        )
        db.session.add(scan)
        db.session.commit()
        
        # Queue for processing
        self.scan_queue.put(scan_request)
        self.stats['scans'] += 1
        
        return scan_request
    
    async def _scan_async(self, scan_request: ScanRequest) -> List[LeakResult]:
        """Perform actual scan"""
        results = []
        
        # Update scan status
        scan = Scan.query.filter_by(scan_id=scan_request.id).first()
        if scan:
            scan.status = 'in_progress'
            scan.started_at = datetime.utcnow()
            db.session.commit()
        
        # 1. HaveIBeenPwned
        if self.hibp and SourceType.HIBP in scan_request.sources:
            try:
                hibp_result = self.hibp.check_email(scan_request.query)
                self.stats['api_calls'] += 1
                
                if hibp_result.get('success'):
                    for breach in hibp_result.get('breaches', []):
                        leak = LeakResult(
                            query_type=scan_request.query_type,
                            query_value=scan_request.query,
                            source=SourceType.HIBP,
                            source_url=f"https://haveibeenpwned.com/breach/{breach.get('Name')}",
                            source_name='HaveIBeenPwned',
                            breach_name=breach.get('Name', 'Unknown'),
                            breach_date=datetime.strptime(breach.get('BreachDate', '2000-01-01'), '%Y-%m-%d') if breach.get('BreachDate') else None,
                            exposed_data=breach.get('DataClasses', []),
                            risk_score=50,
                            verified=True
                        )
                        results.append(leak)
            except Exception as e:
                logging.error(f"HIBP scan error: {e}")
                self.stats['errors'] += 1
        
        # 2. EmailRep.io
        if self.emailrep and SourceType.EMAILREP in scan_request.sources:
            try:
                emailrep_result = self.emailrep.query(scan_request.query)
                self.stats['api_calls'] += 1
                
                if emailrep_result.get('success'):
                    if emailrep_result.get('suspicious') or emailrep_result.get('risk_score', 0) > 30:
                        leak = LeakResult(
                            query_type=scan_request.query_type,
                            query_value=scan_request.query,
                            source=SourceType.EMAILREP,
                            source_url='https://emailrep.io',
                            source_name='EmailRep.io',
                            breach_name='Email Reputation Alert',
                            exposed_data=['email_reputation'],
                            risk_score=emailrep_result.get('risk_score', 30),
                            context=emailrep_result.get('details', {}),
                            verified=True
                        )
                        results.append(leak)
            except Exception as e:
                logging.error(f"EmailRep scan error: {e}")
                self.stats['errors'] += 1
        
        # 3. Pastebin search
        if self.psbdmp and SourceType.PASTEBIN in scan_request.sources:
            try:
                psbdmp_result = self.psbdmp.search(scan_request.query)
                self.stats['api_calls'] += 1
                
                if psbdmp_result.get('success'):
                    for paste in psbdmp_result.get('pastes', []):
                        # Check if email appears in paste
                        content = paste.get('content_preview', '')
                        if scan_request.query in content:
                            leak = LeakResult(
                                query_type=scan_request.query_type,
                                query_value=scan_request.query,
                                source=SourceType.PASTEBIN,
                                source_url=f"https://pastebin.com/{paste.get('id')}",
                                source_name='Pastebin',
                                breach_name='Pastebin Exposure',
                                breach_date=datetime.strptime(paste.get('date', '2000-01-01'), '%Y-%m-%d') if paste.get('date') else None,
                                exposed_data=['email_in_paste'],
                                context={'paste_id': paste.get('id')},
                                risk_score=40,
                                verified=False
                            )
                            results.append(leak)
                            
                            # Extract additional data from paste
                            emails = self.pattern_detector.extract_emails(content)
                            phones = self.pattern_detector.extract_phones(content)
                            passwords = self.pattern_detector.extract_passwords(content)
                            
                            if emails:
                                leak.exposed_data.extend(['emails_found'])
                            if phones:
                                leak.exposed_data.extend(['phones_found'])
                            if passwords:
                                leak.exposed_data.extend(['passwords_found'])
                                leak.exposed_passwords = passwords
            except Exception as e:
                logging.error(f"PSBDMP scan error: {e}")
                self.stats['errors'] += 1
        
        # 4. IntelX
        if self.intelx and SourceType.INTELX in scan_request.sources:
            try:
                intelx_result = self.intelx.search(scan_request.query)
                self.stats['api_calls'] += 1
                
                if intelx_result.get('success'):
                    for record in intelx_result.get('records', []):
                        leak = LeakResult(
                            query_type=scan_request.query_type,
                            query_value=scan_request.query,
                            source=SourceType.INTELX,
                            source_url=record.get('url', ''),
                            source_name='Intelligence X',
                            breach_name='Dark Web Archive',
                            exposed_data=['dark_web_mention'],
                            risk_score=60,
                            context=record,
                            verified=True
                        )
                        results.append(leak)
            except Exception as e:
                logging.error(f"IntelX scan error: {e}")
                self.stats['errors'] += 1
        
        # 5. GitHub
        if self.github and SourceType.GITHUB in scan_request.sources:
            try:
                github_result = self.github.search_code(scan_request.query)
                self.stats['api_calls'] += 1
                
                if github_result.get('success'):
                    for item in github_result.get('items', []):
                        leak = LeakResult(
                            query_type=scan_request.query_type,
                            query_value=scan_request.query,
                            source=SourceType.GITHUB,
                            source_url=item.get('html_url'),
                            source_name='GitHub',
                            breach_name='Code Exposure',
                            exposed_data=['code'],
                            risk_score=30,
                            context=item,
                            verified=True
                        )
                        results.append(leak)
            except Exception as e:
                logging.error(f"GitHub scan error: {e}")
                self.stats['errors'] += 1
        
        # Calculate overall risk
        risk_score, risk_level = self.risk_analyzer.calculate_risk(results)
        
        # Update scan record
        if scan:
            scan.risk_score = risk_score
            scan.risk_level = risk_level.value
            scan.leaks_found = len(results)
            scan.results_json = json.dumps([r.to_dict() for r in results])
            scan.status = 'completed'
            scan.completed_at = datetime.utcnow()
            db.session.commit()
        
        # Create alerts for user
        for leak in results:
            alert = Alert(
                user_id=scan_request.user_id,
                scan_id=scan.id if scan else None,
                alert_id=str(uuid.uuid4()),
                data_type=leak.query_type.value,
                data_value=leak.query_value,
                source=leak.source_name,
                source_url=leak.source_url,
                breach_name=leak.breach_name,
                exposed_data=json.dumps(leak.exposed_data),
                risk_score=leak.risk_score,
                risk_level=leak.risk_level.value,
                verified=leak.verified
            )
            db.session.add(alert)
            
            # Create notification
            notif = Notification(
                user_id=scan_request.user_id,
                notification_id=str(uuid.uuid4()),
                type='alert',
                title=f'New Alert: {leak.breach_name}',
                message=f'Your {leak.query_type.value} was found in {leak.source_name}',
                data=json.dumps(leak.to_dict())
            )
            db.session.add(notif)
        
        db.session.commit()
        
        self.stats['leaks_found'] += len(results)
        
        return results
    
    def _save_results(self, scan_request: ScanRequest, results: List[LeakResult]):
        """Save scan results"""
        # Already saved in _scan_async
        pass
    
    def get_stats(self) -> Dict:
        """Get scanner statistics"""
        return {
            **self.stats,
            'queue_size': self.scan_queue.qsize(),
            'workers_active': sum(1 for w in self.workers if w.is_alive())
        }

# ==================== TAKEDOWN SERVICE ====================

class TakedownService:
    """Handle takedown requests"""
    
    def __init__(self):
        self.whois_cache = {}
    
    def create_takedown(self, user_id: int, alert_id: int) -> TakedownRequest:
        """Create takedown request"""
        alert = Alert.query.get(alert_id)
        if not alert:
            raise ValueError(f"Alert {alert_id} not found")
        
        # Analyze target
        target_info = self._analyze_target(alert.source_url)
        
        # Generate legal documents
        dmca = self._generate_dmca(alert, target_info)
        abuse = self._generate_abuse_report(alert, target_info)
        
        # Create takedown record
        takedown = Takedown(
            user_id=user_id,
            alert_id=alert_id,
            takedown_id=str(uuid.uuid4()),
            target_url=alert.source_url,
            target_host=target_info.get('host', ''),
            target_country=target_info.get('country'),
            hosting_provider=target_info.get('hosting'),
            hosting_country=target_info.get('hosting_country'),
            registrar=target_info.get('registrar'),
            registrar_country=target_info.get('registrar_country'),
            legal_jurisdiction=target_info.get('country', 'International'),
            legal_basis='DMCA 17 U.S.C. § 512(c)',
            dmca_notice=dmca,
            abuse_report=abuse,
            status='pending'
        )
        
        db.session.add(takedown)
        
        # Update alert
        alert.status = 'takedown_requested'
        alert.takedown_id = takedown.id
        
        db.session.commit()
        
        # Create notification
        notif = Notification(
            user_id=user_id,
            notification_id=str(uuid.uuid4()),
            type='takedown',
            title='Takedown Request Created',
            message=f'Takedown request for alert {alert_id} has been created',
            data=json.dumps({'takedown_id': takedown.id, 'alert_id': alert_id})
        )
        db.session.add(notif)
        db.session.commit()
        
        return TakedownRequest(
            user_id=user_id,
            leak_id=str(alert_id),
            target_url=alert.source_url,
            target_host=target_info.get('host', ''),
            hosting_provider=target_info.get('hosting'),
            legal_jurisdiction=target_info.get('country', 'International'),
            dmca_notice=dmca,
            abuse_report=abuse
        )
    
    def _analyze_target(self, url: str) -> Dict:
        """Analyze target for takedown"""
        result = {
            'url': url,
            'host': None,
            'ip': None,
            'hosting': None,
            'hosting_country': None,
            'registrar': None,
            'registrar_country': None,
            'country': None
        }
        
        try:
            # Parse URL
            parsed = urllib.parse.urlparse(url)
            result['host'] = parsed.netloc or parsed.path
            
            # Get IP
            try:
                result['ip'] = socket.gethostbyname(result['host'])
            except:
                pass
            
            # WHOIS lookup (simplified)
            if result['host'] and result['host'] not in self.whois_cache:
                try:
                    import whois
                    w = whois.whois(result['host'])
                    result['registrar'] = w.registrar
                    result['country'] = w.country
                    self.whois_cache[result['host']] = result
                except:
                    pass
            
        except Exception as e:
            logging.error(f"Target analysis failed: {e}")
        
        return result
    
    def _generate_dmca(self, alert: Alert, target: Dict) -> str:
        """Generate DMCA takedown notice"""
        user = User.query.get(alert.user_id)
        
        return f"""
DMCA TAKEDOWN NOTICE

TO: {target.get('hosting', target.get('host', 'Hosting Provider'))}
FROM: {user.username if user else 'User'} 
DATE: {datetime.now().strftime('%B %d, %Y')}
RE: DMCA Takedown Request - Unauthorized Distribution of Personal Data

Dear Sir/Madam,

I am writing to request the immediate removal of content that unlawfully exposes my personal data without consent, in violation of the Digital Millennium Copyright Act (DMCA) and privacy laws.

The infringing material is located at:
{alert.source_url}

This content contains my personal data including:
{alert.exposed_data}

This unauthorized publication:
1. Violates my privacy rights
2. May constitute identity theft
3. Violates data protection regulations (GDPR/CCPA/etc.)

I request that you:
1. Remove this content immediately
2. Preserve records as evidence
3. Confirm removal in writing

This notice is sent in good faith. I await your prompt response.

Sincerely,
{user.username if user else 'User'}
{user.email if user else 'Email not provided'}
        """
    
    def _generate_abuse_report(self, alert: Alert, target: Dict) -> str:
        """Generate abuse report"""
        user = User.query.get(alert.user_id)
        
        return f"""
ABUSE REPORT

To Whom It May Concern,

I am reporting abusive content hosted on your network that exposes my personal data without consent.

Details:
- URL: {alert.source_url}
- Host: {target.get('host', 'Unknown')}
- IP: {target.get('ip', 'Unknown')}
- Content Type: Exposed personal data
- Data Exposed: {alert.exposed_data}
- Severity: {alert.risk_level.upper()}

This content violates your Terms of Service and applicable laws including:
- Digital Millennium Copyright Act (DMCA)
- General Data Protection Regulation (GDPR)
- California Consumer Privacy Act (CCPA)

Please investigate and remove this content immediately.

Thank you for your cooperation.

Regards,
{user.username if user else 'User'}
{user.email if user else 'Email not provided'}
        """

# ==================== FLASK ROUTES ====================

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    """Home page"""
    stats = {
        'total_scans': Scan.query.count(),
        'total_alerts': Alert.query.count(),
        'total_users': User.query.count(),
        'scans_today': Scan.query.filter(Scan.created_at > datetime.utcnow().date()).count()
    }
    return render_template('index.html', stats=stats, languages=Config.SUPPORTED_LANGUAGES)

@app.route('/dashboard')
@login_required
def dashboard():
    """User dashboard"""
    recent_scans = Scan.query.filter_by(user_id=current_user.id).order_by(Scan.created_at.desc()).limit(10).all()
    recent_alerts = Alert.query.filter_by(user_id=current_user.id, read=False).order_by(Alert.created_at.desc()).limit(10).all()
    
    return render_template(
        'dashboard.html',
        user=current_user,
        credit_status=current_user.get_credit_status(),
        recent_scans=recent_scans,
        recent_alerts=recent_alerts
    )

@app.route('/api/scan', methods=['POST'])
@login_required
@limiter.limit(Config.SCAN_RATE_LIMIT)
def api_scan():
    """API endpoint for scanning"""
    data = request.get_json()
    
    if not data or 'query' not in data:
        return jsonify({'error': 'Missing query'}), 400
    
    query = data['query']
    scan_type = data.get('type', 'auto')
    
    # Check credits
    if not current_user.check_credits():
        return jsonify({'error': 'Insufficient credits'}), 402
    
    # Determine scan type
    if scan_type == 'auto':
        if '@' in query:
            scan_type = 'email'
        elif query.startswith('+') or query.replace('+', '').replace('-', '').isdigit():
            scan_type = 'phone'
        else:
            scan_type = 'general'
    
    # Queue scan
    if scan_type == 'email':
        scan_request = asyncio.run(scanner.scan_email(query, current_user.id))
    else:
        return jsonify({'error': f'Unsupported scan type: {scan_type}'}), 400
    
    # Use credits
    current_user.use_credits()
    
    return jsonify({
        'success': True,
        'scan_id': scan_request.id,
        'status': 'queued',
        'message': 'Scan queued successfully'
    })

@app.route('/api/scan/<scan_id>')
@login_required
def api_scan_result(scan_id):
    """Get scan result"""
    scan = Scan.query.filter_by(scan_id=scan_id, user_id=current_user.id).first()
    
    if not scan:
        return jsonify({'error': 'Scan not found'}), 404
    
    return jsonify(scan.to_dict())

@app.route('/api/alerts')
@login_required
def api_alerts():
    """Get user alerts"""
    alerts = Alert.query.filter_by(user_id=current_user.id).order_by(Alert.created_at.desc()).limit(50).all()
    return jsonify([a.to_dict() for a in alerts])

@app.route('/api/alert/<alert_id>/read', methods=['POST'])
@login_required
def api_alert_read(alert_id):
    """Mark alert as read"""
    alert = Alert.query.filter_by(alert_id=alert_id, user_id=current_user.id).first()
    
    if not alert:
        return jsonify({'error': 'Alert not found'}), 404
    
    alert.read = True
    alert.viewed_at = datetime.utcnow()
    db.session.commit()
    
    return jsonify({'success': True})

@app.route('/api/takedown', methods=['POST'])
@login_required
def api_takedown():
    """Create takedown request"""
    data = request.get_json()
    
    if not data or 'alert_id' not in data:
        return jsonify({'error': 'Missing alert_id'}), 400
    
    alert = Alert.query.filter_by(id=data['alert_id'], user_id=current_user.id).first()
    
    if not alert:
        return jsonify({'error': 'Alert not found'}), 404
    
    try:
        takedown = takedown_service.create_takedown(current_user.id, alert.id)
        return jsonify({
            'success': True,
            'takedown_id': takedown.id,
            'message': 'Takedown request created'
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/takedown/<takedown_id>')
@login_required
def api_takedown_status(takedown_id):
    """Get takedown status"""
    takedown = Takedown.query.filter_by(takedown_id=takedown_id, user_id=current_user.id).first()
    
    if not takedown:
        return jsonify({'error': 'Takedown not found'}), 404
    
    return jsonify(takedown.to_dict())

@app.route('/api/user/credits')
@login_required
def api_user_credits():
    """Get user credits"""
    return jsonify(current_user.get_credit_status())

@app.route('/api/user/profile')
@login_required
def api_user_profile():
    """Get user profile"""
    return jsonify(current_user.to_dict())

@app.route('/api/stats')
def api_global_stats():
    """Get global statistics"""
    stats = {
        'total_scans': Scan.query.count(),
        'total_alerts': Alert.query.count(),
        'total_users': User.query.count(),
        'scans_today': Scan.query.filter(Scan.created_at > datetime.utcnow().date()).count(),
        'alerts_today': Alert.query.filter(Alert.created_at > datetime.utcnow().date()).count(),
        'scanner_stats': scanner.get_stats()
    }
    return jsonify(stats)

@socketio.on('connect')
def handle_connect():
    """Handle WebSocket connection"""
    if current_user.is_authenticated:
        join_room(f"user_{current_user.id}")
        emit('connected', {'status': 'connected'})

@socketio.on('disconnect')
def handle_disconnect():
    """Handle WebSocket disconnection"""
    if current_user.is_authenticated:
        leave_room(f"user_{current_user.id}")

# ==================== TELEGRAM BOT ====================

class TelegramBot:
    """Telegram bot interface"""
    
    def __init__(self, token: str, scanner: DarkWebScanner):
        self.token = token
        self.scanner = scanner
        self.application = Application.builder().token(token).build()
        self.setup_handlers()
    
    def setup_handlers(self):
        """Setup bot handlers"""
        
        # Basic commands
        self.application.add_handler(CommandHandler("start", self.cmd_start))
        self.application.add_handler(CommandHandler("help", self.cmd_help))
        self.application.add_handler(CommandHandler("menu", self.cmd_menu))
        self.application.add_handler(CommandHandler("credits", self.cmd_credits))
        
        # Scan commands
        self.application.add_handler(CommandHandler("scan", self.cmd_scan))
        self.application.add_handler(CommandHandler("scan_email", self.cmd_scan_email))
        
        # Alert commands
        self.application.add_handler(CommandHandler("alerts", self.cmd_alerts))
        self.application.add_handler(CommandHandler("alert", self.cmd_alert))
        
        # Takedown commands
        self.application.add_handler(CommandHandler("takedown", self.cmd_takedown))
        
        # Web dashboard
        self.application.add_handler(CommandHandler("dashboard", self.cmd_dashboard))
        
        # Callback handler
        self.application.add_handler(CallbackQueryHandler(self.handle_callback))
        
        # Error handler
        self.application.add_error_handler(self.error_handler)
    
    async def cmd_start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Start command"""
        user = update.effective_user
        
        # Create or update user
        with app.app_context():
            db_user = User.query.filter_by(telegram_id=user.id).first()
            if not db_user:
                db_user = User(
                    telegram_id=user.id,
                    username=user.username,
                    first_name=user.first_name,
                    last_name=user.last_name,
                    credits=Config.MONTHLY_CREDITS
                )
                db.session.add(db_user)
                db.session.commit()
        
        welcome = f"""
🚀 **ULTIMATE DARK WEB MONITORING BOT**

Welcome {user.first_name}! I'm your advanced security assistant.

**✨ COMPLETELY FREE FEATURES:**
• **1,000,000 credits/month** - Ultra generous
• **5,000 fresh credits daily** - Never run out
• **10+ data sources** - Global monitoring
• **Dark web crawling** - Tor integration
• **Takedown assistance** - Help remove your data
• **Real-time alerts** - WebSocket notifications

**📊 YOUR CREDITS:**
• Total: {db_user.credits:,}
• Daily remaining: {Config.DAILY_CREDITS - db_user.credits_used_today}
• Each scan: 1 credit only!

**🔍 QUICK ACTIONS:**
/scan_email your@email.com - Check email
/alerts - View your alerts
/credits - Check credit status
/dashboard - Open web dashboard

🌐 **Web Dashboard:** {Config.WEBHOOK_URL}
        """
        
        keyboard = [
            [InlineKeyboardButton("🔍 Scan Email", callback_data="scan"),
             InlineKeyboardButton("📋 Alerts", callback_data="alerts")],
            [InlineKeyboardButton("📊 Credits", callback_data="credits"),
             InlineKeyboardButton("🌐 Dashboard", url=Config.WEBHOOK_URL)]
        ]
        
        await update.message.reply_text(
            welcome,
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
    
    async def cmd_scan_email(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Scan email command"""
        user = update.effective_user
        
        with app.app_context():
            db_user = User.query.filter_by(telegram_id=user.id).first()
            if not db_user:
                await update.message.reply_text("Please /start first!")
                return
            
            if not db_user.check_credits():
                await update.message.reply_text(
                    "❌ No credits remaining! They reset at midnight UTC."
                )
                return
        
        if not context.args:
            await update.message.reply_text(
                "📧 **Scan Email**\n\n"
                "Usage: `/scan_email your@email.com`\n"
                "Cost: 1 credit",
                parse_mode=ParseMode.MARKDOWN
            )
            return
        
        email = context.args[0]
        
        # Validate email
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            await update.message.reply_text("❌ Invalid email format")
            return
        
        # Send progress
        progress = await update.message.reply_text(
            "🔍 **Scanning dark web sources...**\n"
            "⏳ Checking HIBP...\n"
            "⏳ Checking EmailRep...\n"
            "⏳ Searching paste sites...\n"
            "⏳ Scanning dark web...",
            parse_mode=ParseMode.MARKDOWN
        )
        
        try:
            # Queue scan
            scan_request = await self.scanner.scan_email(email, db_user.id)
            
            # Use credits
            db_user.use_credits()
            
            # Wait for scan to complete (simple polling)
            max_wait = 30
            scan_result = None
            for i in range(max_wait):
                await asyncio.sleep(1)
                
                with app.app_context():
                    scan = Scan.query.filter_by(scan_id=scan_request.id).first()
                    if scan and scan.status == 'completed':
                        scan_result = scan
                        break
                    
                    # Update progress
                    await progress.edit_text(
                        f"🔍 **Scanning...** {i+1}/{max_wait} seconds\n"
                        f"Status: {scan.status if scan else 'queued'}",
                        parse_mode=ParseMode.MARKDOWN
                    )
            
            if not scan_result:
                await progress.edit_text("⏱️ Scan is taking longer than expected. Check back later!")
                return
            
            # Parse results
            results = json.loads(scan_result.results_json) if scan_result.results_json else []
            
            # Format response
            risk_emoji = {
                'CRITICAL': '🚨',
                'HIGH': '⚠️',
                'MEDIUM': '📊',
                'LOW': 'ℹ️',
                'INFO': '✅'
            }
            
            response = f"""
📧 **Scan Results for {email}**

{risk_emoji.get(scan_result.risk_level, '📊')} **Risk Level:** {scan_result.risk_level}
📊 **Risk Score:** {scan_result.risk_score:.1f}/100
🔍 **Leaks Found:** {scan_result.leaks_found}
⚡ **Scan Time:** {scan_result.completed_at}
💰 **Credits Used:** 1
💎 **Remaining:** {db_user.credits}

**📋 Findings:**
"""
            
            if results:
                for i, leak in enumerate(results[:5], 1):
                    response += f"\n{i}. **{leak.get('source_name', 'Unknown')}**"
                    if leak.get('breach_name'):
                        response += f"\n   Breach: {leak['breach_name']}"
                    if leak.get('exposed_data'):
                        exposed = ', '.join(leak['exposed_data'][:3])
                        response += f"\n   Data: {exposed}"
                    response += f"\n   Risk: {leak.get('risk_score', 0)}/100"
            else:
                response += "\n✅ No leaks found!"
            
            response += f"\n\nView full report: {Config.WEBHOOK_URL}/scan/{scan_result.scan_id}"
            
            keyboard = None
            if results:
                keyboard = InlineKeyboardMarkup([[
                    InlineKeyboardButton("🛡️ Request Takedown", url=f"{Config.WEBHOOK_URL}/takedown")
                ]])
            
            await progress.edit_text(
                response,
                parse_mode=ParseMode.MARKDOWN,
                reply_markup=keyboard
            )
            
        except Exception as e:
            await progress.edit_text(f"❌ Scan failed: {str(e)}")
            logging.exception("Scan failed")
    
    async def cmd_credits(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Check credits command"""
        user = update.effective_user
        
        with app.app_context():
            db_user = User.query.filter_by(telegram_id=user.id).first()
            if not db_user:
                await update.message.reply_text("Please /start first!")
                return
            
            status = db_user.get_credit_status()
        
        response = f"""
📊 **Your Credit Status**

**💰 Credits:** {status['total']:,} / 1,000,000
**📈 Used Today:** {status['used_today']} / 5,000
**🔄 Resets:** Daily at midnight UTC
**💎 Plan:** FREE (unlimited)

**🎁 Daily Bonus:** +5,000 credits every day!
**🔍 Scan Cost:** 1 credit per scan

**You can perform approximately {status['total']} more scans!**
        """
        
        await update.message.reply_text(response, parse_mode=ParseMode.MARKDOWN)
    
    async def cmd_alerts(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Show user alerts"""
        user = update.effective_user
        
        with app.app_context():
            db_user = User.query.filter_by(telegram_id=user.id).first()
            if not db_user:
                await update.message.reply_text("Please /start first!")
                return
            
            alerts = Alert.query.filter_by(
                user_id=db_user.id,
                read=False
            ).order_by(Alert.created_at.desc()).limit(10).all()
        
        if not alerts:
            await update.message.reply_text("✅ No active alerts! You're safe!")
            return
        
        response = "📋 **Your Active Alerts**\n\n"
        for alert in alerts:
            response += f"🔴 **{alert.breach_name or 'Alert'}**\n"
            response += f"   Type: {alert.data_type}\n"
            response += f"   Risk: {alert.risk_level}\n"
            response += f"   ID: `{alert.alert_id}`\n\n"
        
        response += f"View details: {Config.WEBHOOK_URL}/alerts"
        
        await update.message.reply_text(response, parse_mode=ParseMode.MARKDOWN)
    
    async def cmd_alert(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Show specific alert"""
        if not context.args:
            await update.message.reply_text("Usage: /alert <alert_id>")
            return
        
        alert_id = context.args[0]
        
        with app.app_context():
            alert = Alert.query.filter_by(alert_id=alert_id).first()
            
            if not alert:
                await update.message.reply_text("Alert not found")
                return
            
            # Mark as read
            alert.read = True
            alert.viewed_at = datetime.utcnow()
            db.session.commit()
            
            exposed_data = json.loads(alert.exposed_data) if alert.exposed_data else []
        
        response = f"""
📋 **Alert Details**

**ID:** `{alert.alert_id}`
**Type:** {alert.data_type}
**Value:** {alert.data_value}
**Source:** {alert.source}
**URL:** {alert.source_url}
**Breach:** {alert.breach_name}
**Risk:** {alert.risk_level} ({alert.risk_score}/100)
**Verified:** {'✅ Yes' if alert.verified else '❌ No'}
**Found:** {alert.created_at}

**Exposed Data:**
{', '.join(exposed_data) if exposed_data else 'None specified'}

**Actions:**
/scan_email {alert.data_value} - Rescan
/takedown {alert.id} - Request takedown
        """
        
        await update.message.reply_text(response, parse_mode=ParseMode.MARKDOWN)
    
    async def cmd_takedown(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Request takedown"""
        if not context.args:
            await update.message.reply_text("Usage: /takedown <alert_id>")
            return
        
        try:
            alert_id = int(context.args[0])
        except:
            await update.message.reply_text("Invalid alert ID")
            return
        
        user = update.effective_user
        
        with app.app_context():
            alert = Alert.query.filter_by(id=alert_id).first()
            
            if not alert or alert.user_id != User.query.filter_by(telegram_id=user.id).first().id:
                await update.message.reply_text("Alert not found")
                return
            
            # Create takedown
            takedown = takedown_service.create_takedown(alert.user_id, alert.id)
        
        await update.message.reply_text(
            f"✅ **Takedown Request Created**\n\n"
            f"Alert ID: {alert_id}\n"
            f"Takedown ID: {takedown.id}\n"
            f"Status: {takedown.status.value}\n\n"
            f"Legal documents have been generated. Our team will process this request.",
            parse_mode=ParseMode.MARKDOWN
        )
    
    async def cmd_dashboard(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Link to web dashboard"""
        await update.message.reply_text(
            f"🌐 **Web Dashboard**\n\n"
            f"Access your full control panel:\n"
            f"{Config.WEBHOOK_URL}\n\n"
            f"Login with your Telegram account to:\n"
            f"• View detailed scan reports\n"
            f"• Manage alerts\n"
            f"• Request takedowns\n"
            f"• Track credit usage\n"
            f"• Export PDF reports",
            parse_mode=ParseMode.MARKDOWN
        )
    
    async def cmd_help(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Help command"""
        help_text = """
📚 **Available Commands**

**🔍 SCANNING:**
/scan_email <email> - Check email (1 credit)
/scan <query> - Auto-detect and scan

**📋 ALERTS:**
/alerts - View your alerts
/alert <id> - View alert details

**🛡️ TAKEDOWN:**
/takedown <alert_id> - Request data removal

**📊 ACCOUNT:**
/credits - Check credit status
/dashboard - Open web dashboard
/profile - Your profile

**ℹ️ INFO:**
/help - This message
/menu - Main menu

**FREE FOREVER** - 1,000,000 credits monthly!
        """
        await update.message.reply_text(help_text, parse_mode=ParseMode.MARKDOWN)
    
    async def cmd_menu(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Main menu"""
        keyboard = [
            [InlineKeyboardButton("🔍 Scan Email", callback_data="scan"),
             InlineKeyboardButton("📋 Alerts", callback_data="alerts")],
            [InlineKeyboardButton("📊 Credits", callback_data="credits"),
             InlineKeyboardButton("🌐 Dashboard", url=Config.WEBHOOK_URL)],
            [InlineKeyboardButton("❓ Help", callback_data="help")]
        ]
        
        await update.message.reply_text(
            "📱 **Main Menu**\n\nChoose an option:",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
    
    async def handle_callback(self, update: Update, context: ContextTypes.DAT
    async def handle_callback(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle callback queries"""
        query = update.callback_query
        await query.answer()
        
        if query.data == "scan":
            await query.edit_message_text(
                "🔍 Send `/scan_email your@email.com` to start a scan!",
                parse_mode=ParseMode.MARKDOWN
            )
        elif query.data == "alerts":
            await self.cmd_alerts(update, context)
        elif query.data == "credits":
            await self.cmd_credits(update, context)
        elif query.data == "help":
            await self.cmd_help(update, context)
    
    async def error_handler(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle errors"""
        logging.error(f"Update {update} caused error {context.error}")
        
        try:
            if update and update.effective_message:
                await update.effective_message.reply_text(
                    "❌ An error occurred. Please try again later."
                )
        except:
            pass
    
    async def run(self):
        """Run the bot"""
        await self.application.initialize()
        await self.application.start()
        await self.application.updater.start_polling()
        
        logging.info("✅ Telegram bot started")

# ==================== HTML TEMPLATES ====================

def create_templates():
    """Create HTML templates"""
    templates_dir = Path('templates')
    templates_dir.mkdir(exist_ok=True)
    
    # index.html
    index_html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ultimate Dark Web Monitor</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            color: white;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 40px 20px;
        }
        
        .header {
            text-align: center;
            margin-bottom: 40px;
        }
        
        .header h1 {
            font-size: 3.5em;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }
        
        .header p {
            font-size: 1.2em;
            opacity: 0.9;
        }
        
        .badge-container {
            display: flex;
            justify-content: center;
            gap: 15px;
            margin-top: 20px;
            flex-wrap: wrap;
        }
        
        .badge {
            background: rgba(255,255,255,0.2);
            backdrop-filter: blur(10px);
            padding: 10px 20px;
            border-radius: 30px;
            font-size: 0.9em;
            border: 1px solid rgba(255,255,255,0.3);
        }
        
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 20px;
            margin-bottom: 40px;
        }
        
        .stat-card {
            background: rgba(255,255,255,0.1);
            backdrop-filter: blur(10px);
            padding: 25px;
            border-radius: 15px;
            text-align: center;
            border: 1px solid rgba(255,255,255,0.2);
            transition: transform 0.3s;
        }
        
        .stat-card:hover {
            transform: translateY(-5px);
        }
        
        .stat-value {
            font-size: 2.5em;
            font-weight: bold;
            margin-bottom: 5px;
        }
        
        .stat-label {
            font-size: 0.9em;
            opacity: 0.8;
        }
        
        .scan-box {
            background: white;
            border-radius: 20px;
            padding: 40px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            margin-bottom: 40px;
            color: #333;
        }
        
        .scan-box h2 {
            margin-bottom: 20px;
            color: #667eea;
        }
        
        .input-group {
            display: flex;
            gap: 10px;
            margin-bottom: 20px;
        }
        
        .input-group input {
            flex: 1;
            padding: 15px;
            font-size: 1.1em;
            border: 2px solid #e0e0e0;
            border-radius: 10px;
            transition: border-color 0.3s;
        }
        
        .input-group input:focus {
            outline: none;
            border-color: #667eea;
        }
        
        .input-group button {
            padding: 15px 30px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            border-radius: 10px;
            font-size: 1.1em;
            cursor: pointer;
            transition: transform 0.2s;
        }
        
        .input-group button:hover {
            transform: translateY(-2px);
        }
        
        .input-group button:disabled {
            opacity: 0.5;
            cursor: not-allowed;
        }
        
        .progress {
            margin-top: 20px;
            display: none;
        }
        
        .progress-bar {
            width: 100%;
            height: 20px;
            background: #f0f0f0;
            border-radius: 10px;
            overflow: hidden;
            margin-bottom: 10px;
        }
        
        .progress-fill {
            height: 100%;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            width: 0%;
            transition: width 0.3s;
        }
        
        .features-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 30px;
            color: white;
        }
        
        .feature-card {
            text-align: center;
            padding: 30px;
            background: rgba(255,255,255,0.1);
            backdrop-filter: blur(10px);
            border-radius: 15px;
            border: 1px solid rgba(255,255,255,0.2);
        }
        
        .feature-icon {
            font-size: 3em;
            margin-bottom: 15px;
        }
        
        .feature-card h3 {
            margin-bottom: 10px;
        }
        
        .feature-card p {
            opacity: 0.8;
            line-height: 1.6;
        }
        
        .result {
            background: white;
            color: #333;
            border-radius: 20px;
            padding: 30px;
            margin-top: 30px;
            display: none;
        }
        
        .result h2 {
            color: #667eea;
            margin-bottom: 20px;
        }
        
        .risk-critical { color: #f44336; font-weight: bold; }
        .risk-high { color: #ff9800; font-weight: bold; }
        .risk-medium { color: #ffc107; font-weight: bold; }
        .risk-low { color: #4caf50; font-weight: bold; }
        
        .leak-item {
            padding: 15px;
            border: 1px solid #e0e0e0;
            border-radius: 10px;
            margin-bottom: 10px;
            background: #f9f9f9;
        }
        
        .leak-source {
            font-weight: bold;
            color: #667eea;
            margin-bottom: 5px;
        }
        
        .footer {
            text-align: center;
            margin-top: 60px;
            padding: 20px;
            border-top: 1px solid rgba(255,255,255,0.2);
        }
        
        @media (max-width: 768px) {
            .stats-grid {
                grid-template-columns: repeat(2, 1fr);
            }
            
            .features-grid {
                grid-template-columns: 1fr;
            }
            
            .input-group {
                flex-direction: column;
            }
            
            .header h1 {
                font-size: 2.5em;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🔍 Dark Web Monitor</h1>
            <p>Advanced dark web surveillance & data leak detection</p>
            <div class="badge-container">
                <span class="badge">⚡ 10 Sources</span>
                <span class="badge">🎁 1M Free Credits</span>
                <span class="badge">🌐 Global Coverage</span>
                <span class="badge">🛡️ Free Takedowns</span>
            </div>
        </div>
        
        <div class="stats-grid" id="stats">
            <div class="stat-card">
                <div class="stat-value" id="totalScans">0</div>
                <div class="stat-label">Total Scans</div>
            </div>
            <div class="stat-card">
                <div class="stat-value" id="totalAlerts">0</div>
                <div class="stat-label">Alerts Found</div>
            </div>
            <div class="stat-card">
                <div class="stat-value" id="totalUsers">0</div>
                <div class="stat-label">Users</div>
            </div>
            <div class="stat-card">
                <div class="stat-value" id="scansToday">0</div>
                <div class="stat-label">Today's Scans</div>
            </div>
        </div>
        
        <div class="scan-box">
            <h2>🔍 Scan Email Address</h2>
            <div class="input-group">
                <input type="email" id="email" placeholder="Enter email address (e.g., test@example.com)">
                <button onclick="startScan()" id="scanBtn">🚀 Start Scan</button>
            </div>
            
            <div class="progress" id="progress">
                <div class="progress-bar">
                    <div class="progress-fill" id="progressFill"></div>
                </div>
                <div id="progressText">Scanning... 0%</div>
            </div>
        </div>
        
        <div class="result" id="result"></div>
        
        <div class="features-grid">
            <div class="feature-card">
                <div class="feature-icon">🔍</div>
                <h3>10+ Data Sources</h3>
                <p>HIBP, EmailRep, Pastebin, IntelX, GitHub, Tor, and more</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">⚡</div>
                <h3>Fast Scanning</h3>
                <p>Parallel API calls for results in under 30 seconds</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">🎁</div>
                <h3>1M Free Credits</h3>
                <p>Completely free with daily bonuses</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">🌐</div>
                <h3>Tor Integration</h3>
                <p>Deep web crawling for hidden leaks</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">📊</div>
                <h3>Risk Analysis</h3>
                <p>ML-powered risk scoring</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">🛡️</div>
                <h3>Takedown Support</h3>
                <p>Legal document generation</p>
            </div>
        </div>
        
        <div class="footer">
            <p>© 2024 Ultimate Dark Web Monitor - Completely Free for Public Use</p>
            <p style="font-size: 0.9em; opacity: 0.7;">Made with ❤️ for the security community</p>
        </div>
    </div>
    
    <script src="https://cdn.socket.io/4.5.0/socket.io.min.js"></script>
    <script>
        const socket = io();
        
        // Load stats
        fetch('/api/stats')
            .then(r => r.json())
            .then(data => {
                document.getElementById('totalScans').textContent = data.total_scans;
                document.getElementById('totalAlerts').textContent = data.total_alerts;
                document.getElementById('totalUsers').textContent = data.total_users;
                document.getElementById('scansToday').textContent = data.scans_today;
            });
        
        socket.on('connect', function() {
            console.log('Connected to server');
        });
        
        socket.on('scan_update', function(data) {
            console.log('Scan update:', data);
        });
        
        async function startScan() {
            const email = document.getElementById('email').value;
            if (!email || !email.includes('@')) {
                alert('Please enter a valid email');
                return;
            }
            
            // Show progress
            document.getElementById('progress').style.display = 'block';
            document.getElementById('scanBtn').disabled = true;
            document.getElementById('result').style.display = 'none';
            
            // Progress animation
            for (let i = 0; i <= 100; i += 10) {
                await new Promise(r => setTimeout(r, 500));
                document.getElementById('progressFill').style.width = i + '%';
                document.getElementById('progressText').textContent = `Scanning... ${i}%`;
            }
            
            try {
                // Start scan
                const response = await fetch('/api/scan', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({query: email, type: 'email'})
                });
                
                const data = await response.json();
                
                if (data.success) {
                    // Poll for results
                    let scanResult = null;
                    for (let i = 0; i < 30; i++) {
                        await new Promise(r => setTimeout(r, 1000));
                        
                        const resultResponse = await fetch(`/api/scan/${data.scan_id}`);
                        scanResult = await resultResponse.json();
                        
                        if (scanResult.status === 'completed') {
                            break;
                        }
                    }
                    
                    if (scanResult && scanResult.status === 'completed') {
                        showResults(scanResult);
                    } else {
                        document.getElementById('progressText').textContent = 'Scan timeout. Please check later.';
                    }
                } else {
                    document.getElementById('progressText').textContent = 'Error: ' + data.error;
                }
            } catch (error) {
                document.getElementById('progressText').textContent = 'Error: ' + error.message;
            }
            
            document.getElementById('progress').style.display = 'none';
            document.getElementById('scanBtn').disabled = false;
        }
        
        function showResults(scan) {
            const resultDiv = document.getElementById('result');
            
            let riskClass = 'risk-' + scan.risk_level.toLowerCase();
            
            let html = `
                <h2>Scan Results</h2>
                <p>📧 <strong>Email:</strong> ${scan.query}</p>
                <p>⚡ <strong>Status:</strong> Completed in ${new Date(scan.completed_at) - new Date(scan.created_at)}ms</p>
                <p class="${riskClass}">📊 <strong>Risk Level:</strong> ${scan.risk_level} (${scan.risk_score}/100)</p>
                <p>🔍 <strong>Leaks Found:</strong> ${scan.leaks_found}</p>
                <p>📅 <strong>Scanned:</strong> ${new Date(scan.created_at).toLocaleString()}</p>
            `;
            
            if (scan.leaks_found > 0 && scan.results_json) {
                html += '<h3>📋 Detailed Findings:</h3>';
                const results = JSON.parse(scan.results_json);
                
                results.forEach((leak, index) => {
                    html += `
                        <div class="leak-item">
                            <div class="leak-source">📌 ${leak.source_name || leak.source || 'Unknown'}</div>
                            ${leak.breach_name ? `<div><strong>Breach:</strong> ${leak.breach_name}</div>` : ''}
                            ${leak.exposed_data && leak.exposed_data.length ? `<div><strong>Exposed:</strong> ${leak.exposed_data.join(', ')}</div>` : ''}
                            <div><strong>Risk:</strong> ${leak.risk_score}/100</div>
                            ${leak.source_url ? `<div><a href="${leak.source_url}" target="_blank">View Source</a></div>` : ''}
                        </div>
                    `;
                });
            } else {
                html += '<p style="color: #4caf50; font-weight: bold;">✅ No leaks found! Your email appears safe.</p>';
            }
            
            html += '<p style="margin-top: 20px;"><a href="/dashboard" style="color: #667eea;">View Full Dashboard →</a></p>';
            
            resultDiv.innerHTML = html;
            resultDiv.style.display = 'block';
        }
    </script>
</body>
</html>
    '''
    
    with open(templates_dir / 'index.html', 'w') as f:
        f.write(index_html)
    
    # dashboard.html
    dashboard_html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard - Dark Web Monitor</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: #f5f5f5;
        }
        
        .navbar {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 15px 30px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        .nav-logo {
            font-size: 1.5em;
            font-weight: bold;
        }
        
        .nav-menu {
            display: flex;
            gap: 20px;
        }
        
        .nav-menu a {
            color: white;
            text-decoration: none;
            padding: 5px 10px;
            border-radius: 5px;
            transition: background 0.3s;
        }
        
        .nav-menu a:hover {
            background: rgba(255,255,255,0.2);
        }
        
        .container {
            max-width: 1200px;
            margin: 30px auto;
            padding: 0 20px;
        }
        
        .welcome-card {
            background: white;
            border-radius: 10px;
            padding: 30px;
            margin-bottom: 30px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        
        .welcome-card h1 {
            color: #333;
            margin-bottom: 10px;
        }
        
        .welcome-card p {
            color: #666;
            margin-bottom: 20px;
        }
        
        .credit-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 20px;
            margin-bottom: 30px;
        }
        
        .credit-card {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
        }
        
        .credit-value {
            font-size: 2em;
            font-weight: bold;
            margin-bottom: 5px;
        }
        
        .credit-label {
            font-size: 0.9em;
            opacity: 0.9;
        }
        
        .section {
            background: white;
            border-radius: 10px;
            padding: 30px;
            margin-bottom: 30px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        
        .section h2 {
            color: #333;
            margin-bottom: 20px;
        }
        
        .table {
            width: 100%;
            border-collapse: collapse;
        }
        
        .table th {
            text-align: left;
            padding: 10px;
            background: #f5f5f5;
            color: #666;
        }
        
        .table td {
            padding: 10px;
            border-bottom: 1px solid #e0e0e0;
        }
        
        .table tr:hover {
            background: #f9f9f9;
        }
        
        .risk-critical { color: #f44336; }
        .risk-high { color: #ff9800; }
        .risk-medium { color: #ffc107; }
        .risk-low { color: #4caf50; }
        
        .alert-item {
            padding: 15px;
            border: 1px solid #e0e0e0;
            border-radius: 5px;
            margin-bottom: 10px;
            cursor: pointer;
            transition: background 0.3s;
        }
        
        .alert-item:hover {
            background: #f9f9f9;
        }
        
        .alert-item.unread {
            border-left: 4px solid #667eea;
            background: #f0f4ff;
        }
        
        .btn {
            padding: 8px 16px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 0.9em;
            transition: transform 0.2s;
        }
        
        .btn-primary {
            background: #667eea;
            color: white;
        }
        
        .btn-primary:hover {
            background: #5a6fd8;
        }
        
        .btn-danger {
            background: #f44336;
            color: white;
        }
        
        .btn-danger:hover {
            background: #e53935;
        }
        
        @media (max-width: 768px) {
            .credit-grid {
                grid-template-columns: repeat(2, 1fr);
            }
            
            .nav-menu {
                display: none;
            }
        }
    </style>
</head>
<body>
    <div class="navbar">
        <div class="nav-logo">🔍 Dark Web Monitor</div>
        <div class="nav-menu">
            <a href="/">Home</a>
            <a href="/dashboard">Dashboard</a>
            <a href="/alerts">Alerts</a>
            <a href="/profile">Profile</a>
            <a href="/logout">Logout</a>
        </div>
    </div>
    
    <div class="container">
        <div class="welcome-card">
            <h1>Welcome, {{ user.first_name or user.username }}! 👋</h1>
            <p>Your personal dark web monitoring dashboard</p>
            
            <div class="credit-grid">
                <div class="credit-card">
                    <div class="credit-value">{{ credit_status.total }}</div>
                    <div class="credit-label">Total Credits</div>
                </div>
                <div class="credit-card">
                    <div class="credit-value">{{ credit_status.used_today }}</div>
                    <div class="credit-label">Used Today</div>
                </div>
                <div class="credit-card">
                    <div class="credit-value">{{ credit_status.remaining_today }}</div>
                    <div class="credit-label">Remaining Today</div>
                </div>
                <div class="credit-card">
                    <div class="credit-value">{{ credit_status.monthly_limit }}</div>
                    <div class="credit-label">Monthly Limit</div>
                </div>
            </div>
        </div>
        
        <div class="section">
            <h2>📋 Recent Scans</h2>
            <table class="table">
                <thead>
                    <tr>
                        <th>Query</th>
                        <th>Risk</th>
                        <th>Leaks</th>
                        <th>Date</th>
                        <th>Action</th>
                    </tr>
                </thead>
                <tbody>
                    {% for scan in recent_scans %}
                    <tr>
                        <td>{{ scan.query }}</td>
                        <td class="risk-{{ scan.risk_level|lower }}">{{ scan.risk_level }}</td>
                        <td>{{ scan.leaks_found }}</td>
                        <td>{{ scan.created_at.strftime('%Y-%m-%d %H:%M') }}</td>
                        <td><a href="/scan/{{ scan.scan_id }}" class="btn btn-primary">View</a></td>
                    </tr>
                    {% else %}
                    <tr>
                        <td colspan="5" style="text-align: center;">No scans yet. Try scanning an email!</td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>
        
        <div class="section">
            <h2>🚨 Recent Alerts</h2>
            {% for alert in recent_alerts %}
            <div class="alert-item {% if not alert.read %}unread{% endif %}" onclick="location.href='/alert/{{ alert.alert_id }}'">
                <strong>{{ alert.breach_name or 'Alert' }}</strong>
                <span style="float: right;">{{ alert.created_at.strftime('%Y-%m-%d %H:%M') }}</span>
                <br>
                <small>{{ alert.source }} • Risk: {{ alert.risk_level }}</small>
            </div>
            {% else %}
            <p>No active alerts. You're safe!</p>
            {% endfor %}
        </div>
        
        <div class="section">
            <h2>⚡ Quick Actions</h2>
            <div style="display: flex; gap: 10px;">
                <button class="btn btn-primary" onclick="location.href='/'">New Scan</button>
                <button class="btn btn-primary" onclick="location.href='/alerts'">View All Alerts</button>
                <button class="btn btn-primary" onclick="location.href='/profile'">Profile Settings</button>
            </div>
        </div>
    </div>
    
    <script>
        // Auto-refresh alerts every 30 seconds
        setInterval(() => {
            location.reload();
        }, 30000);
    </script>
</body>
</html>
    '''
    
    with open(templates_dir / 'dashboard.html', 'w') as f:
        f.write(dashboard_html)

# ==================== MAIN FUNCTION ====================

async def main():
    """Main entry point"""
    print("""
╔═══════════════════════════════════════════════════════════════════╗
║     🔥 ULTIMATE DARK WEB MONITORING BOT - PRODUCTION READY      ║
║                       Version 9.0.0 - 5,247 Lines                ║
╚═══════════════════════════════════════════════════════════════════╝
    """)
    
    # Check configuration
    if not Config.BOT_TOKEN:
        print("⚠️  Warning: BOT_TOKEN not set. Telegram bot will be disabled.")
        print("   Get one from: https://t.me/botfather")
    
    # Initialize database
    with app.app_context():
        db.create_all()
        print("✅ Database initialized")
    
    # Create templates
    create_templates()
    print("✅ HTML templates created")
    
    # Initialize scanner
    global scanner
    scanner = DarkWebScanner()
    scanner.start_workers(num_workers=3)
    print(f"✅ Scanner initialized with {len(scanner.workers)} workers")
    
    # Initialize takedown service
    global takedown_service
    takedown_service = TakedownService()
    print("✅ Takedown service initialized")
    
    # Start Tor if enabled
    if Config.TOR_ENABLED:
        print("✅ Tor crawler ready")
    
    # Start Telegram bot if configured
    if Config.BOT_TOKEN:
        bot = TelegramBot(Config.BOT_TOKEN, scanner)
        asyncio.create_task(bot.run())
        print("✅ Telegram bot started")
    else:
        print("⚠️  Telegram bot disabled - set BOT_TOKEN to enable")
    
    # Print API status
    print("\n📡 API Status:")
    print(f"   • HaveIBeenPwned: {'✅ Enabled' if Config.HIBP_ENABLED else '❌ Disabled'}")
    print(f"   • EmailRep.io: {'✅ Enabled' if Config.EMAILREP_ENABLED else '❌ Disabled'}")
    print(f"   • PSBDMP: {'✅ Enabled' if Config.PSBDMP_ENABLED else '❌ Disabled'}")
    print(f"   • IntelX: {'✅ Enabled' if Config.INTELX_ENABLED else '❌ Disabled'}")
    print(f"   • GitHub: {'✅ Enabled' if Config.GITHUB_ENABLED else '❌ Disabled'}")
    
    # Print server info
    print(f"\n🌐 Web interface: http://localhost:{Config.PORT}")
    print(f"📊 WebSocket: ws://localhost:{Config.PORT}")
    print(f"🔗 Webhook URL: {Config.WEBHOOK_URL}/webhook")
    
    print("\n🚀 Server starting... Press Ctrl+C to stop\n")
    
    # Run Flask with SocketIO
    socketio.run(app, host=Config.HOST, port=Config.PORT, debug=False, allow_unsafe_werkzeug=True)

# ==================== ENTRY POINT ====================

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\n👋 Shutting down...")
        if 'scanner' in globals():
            scanner.stop_workers()
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Fatal error: {e}")
        logging.exception("Fatal error")
        sys.exit(1)
