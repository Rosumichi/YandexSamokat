-- Задание 1: Подсчет активных заказов в статусе доставки для курьеров
select 
    cour.login, 
    count(ord.id) as active_delivery_count
from "Couriers" as cour
inner join "Orders" as ord on cour.id = ord."courierId"
where ord."inDelivery" = true
group by cour.login;

-- Задание 2: Формирование статусов заказов по их трекерам
select 
    track,
    case 
        when finished = true then 2
        when cancelled = true then -1
        when "inDelivery" = true then 1
        else 0
    end as order_status
from "Orders";