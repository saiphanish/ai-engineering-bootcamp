from exceptions.invalid_cost import InvalidServiceCost
from services.logger import logger

try:

    cost = float(input("Enter Service Cost: "))

    if cost < 0:

        raise InvalidServiceCost("Cost cannot be negative.")

    logger.info(f"Service Created: {cost}")

    print("Service Created Successfully")

except InvalidServiceCost as ex:

    logger.error(ex)

    print(ex)

except Exception as ex:

    logger.error(ex)

    print(ex)