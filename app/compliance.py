import time, json, os
from flask import g

AUDIT_FILE = 'audit.log'
RETENTION_DAYS = int(os.environ.get('RETENTION_DAYS', '30'))


def audit_log(action, pid):
    user = getattr(g, 'user', {})
    log_entry = {
        'user': user.get('preferred_username', 'unknown'),
        'action': action,
        'patient_id': pid
    }
    print(log_entry)
    # audit persistence can be added later


def data_minimize(payload):
    """
    Return only allowed patient fields (remove sensitive data)
    """
    allowed = {
        k: payload[k]
        for k in ['id', 'name', 'dob', 'consent']
        if k in payload
    }
    return allowed


def enforce_consent(payload):
    if not payload.get('consent', False):
        raise ValueError('Consent required')


def retention_cleanup():
    cutoff = time.time() - RETENTION_DAYS * 24 * 3600
    # stub: remove records older than cutoff
    return cutoff