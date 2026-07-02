from enum import StrEnum

STATUS_CHOICES = (
    ('pending', 'Pending'),
    ('processed', 'Processed'),
    ('failed', 'Failed'),
    ('completed', 'Completed'),
)

class Status(StrEnum):
    PENDING = 'pending'
    PROCESSED = 'processed'
    FAILED = 'failed'
    COMPLETED = 'completed'
