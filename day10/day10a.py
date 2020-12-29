All decisions are based on the number of occupied seats adjacent to a given seat(one of the eight positions immediately up, down, left, right, or diagonal from the seat). The following rules are applied to every seat simultaneously:

If a seat is empty(L) and there are no occupied seats adjacent to it, the seat becomes occupied.
If a seat is occupied(  # ) and four or more seats adjacent to it are also occupied, the seat becomes empty.
Otherwise, the seat's state does not change.
Floor(.) never changes; seats don't move, and nobody sits on the floor.
