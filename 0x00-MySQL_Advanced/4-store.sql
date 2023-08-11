-- creates a trigger that decreases the quantity of an item after adding a new order.
DELIMETER //
CREATE TRIGGER decrease_quanity_on_order
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
  --decrease the quantity in items table upon adding new row
  UPDATE items
  SET quantity = quantity - NEW.number
  WHERE name = NEW.item_name;
END
//
DELIMETER ;
