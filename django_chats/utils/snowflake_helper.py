from snowflake import SnowflakeGenerator

snowflake = SnowflakeGenerator(instance=1)


def get_snowflake_id():
    return next(snowflake)
