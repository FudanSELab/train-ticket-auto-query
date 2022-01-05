from .queries import Query
from .utils import *
import logging

logger = logging.getLogger("autoquery-scenario")
highspeed_weights = {True: 60, False: 40}


def query_and_cancel(q: Query):
    if random_from_weighted(highspeed_weights):
        pairs = q.query_orders(types=tuple([0, 1]))
    else:
        pairs = q.query_orders(types=tuple([0, 1]), query_other=True)

    if not pairs:
        return

    # (orderId, tripId)
    pair = random_form_list(pairs)

    order_id = q.cancel_order(order_id=pair[0])
    if not order_id:
        return

    logger.info(f"{order_id} queried and canceled")


def query_and_collect(q: Query):
    if random_from_weighted(highspeed_weights):
        pairs = q.query_orders(types=tuple([1]))
    else:
        pairs = q.query_orders(types=tuple([1]), query_other=True)

    if not pairs:
        return

    # (orderId, tripId)
    pair = random_form_list(pairs)

    order_id = q.collect_order(order_id=pair[0])
    if not order_id:
        return

    logger.info(f"{order_id} queried and collected")


def query_and_execute(q: Query):
    if random_from_weighted(highspeed_weights):
        pairs = q.query_orders(types=tuple([1]))
    else:
        pairs = q.query_orders(types=tuple([1]), query_other=True)

    if not pairs:
        return

    # (orderId, tripId)
    pair = random_form_list(pairs)

    order_id = q.enter_station(order_id=pair[0])
    if not order_id:
        return

    logger.info(f"{order_id} queried and entered station")


def query_and_preserve(q: Query):
    start = ""
    end = ""
    trip_ids = []

    high_speed = random_from_weighted(highspeed_weights)
    if high_speed:
        start = "Shang Hai"
        end = "Su Zhou"
        high_speed_place_pair = (start, end)
        trip_ids = q.query_high_speed_ticket(place_pair=high_speed_place_pair)
    else:
        start = "Shang Hai"
        end = "Nan Jing"
        other_place_pair = (start, end)
        trip_ids = q.query_normal_ticket(place_pair=other_place_pair)

    _ = q.query_assurances()

    q.preserve(start, end, trip_ids, high_speed)


def query_and_consign(q: Query):
    if random_from_weighted(highspeed_weights):
        pairs = q.query_orders_all_info()
    else:
        pairs = q.query_orders(query_other=True)

    if not pairs:
        return

    # (orderId, tripId)
    pair = random_form_list(pairs)
    order_id = q.put_consign(pair)

    if not order_id:
        return

    logger.info(f"{order_id} queried and put consign")


def query_and_pay(q: Query):
    if random_from_weighted(highspeed_weights):
        pairs = q.query_orders(types=tuple([0, 1]))
    else:
        pairs = q.query_orders(types=tuple([0, 1]), query_other=True)

    if not pairs:
        return

    # (orderId, tripId)
    pair = random_form_list(pairs)
    order_id = q.pay_order(pair[0], pair[1])

    if not order_id:
        return

    logger.info(f"{order_id} queried and paid")
