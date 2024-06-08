from pyuilder import Buildable, Builder, Setter
from dataclasses import dataclass


@dataclass
class Burger(Buildable):
	bun: bool = False
	patty: bool = False
	cheese: bool = False
	bacon: bool = False

	class builder(Builder["Burger"]):
		bun: Setter["Burger.builder", bool]
		patty: Setter["Burger.builder", bool]
