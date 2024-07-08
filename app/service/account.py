import uuid
import datetime
import logging

from ..model.account import Account
from ..db import db
from ..util.dto import AccountDto

logger = logging.getLogger(__name__)


def create_account(account: AccountDto.account) -> Account:
    try:
        new_account = Account(
            public_id=str(uuid.uuid4()),
            email=account['email'],
            username=account['username'],
            password=account['password'],
            registered_on=datetime.datetime.utcnow()
        )
        db.session.add(new_account)
        db.session.commit()
        return new_account
    except Exception as ex:
        db.session.rollback()
        logger.error(f"Can not create account! Error: {ex}")
        return None

def get_account_by_id(id: str) -> AccountDto.account:
    return Account.query.filter_by(public_id=id).first()

def get_all_accounts() -> list[Account]:
    return Account.query.all()