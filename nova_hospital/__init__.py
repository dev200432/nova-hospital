from django.db.backends.base.base import BaseDatabaseWrapper

def skip_db_version_check(self):
    pass

BaseDatabaseWrapper.check_database_version_supported = skip_db_version_check