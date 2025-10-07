# ir.py
from dataclasses import dataclass
from typing import Any, Dict, List, Literal, Optional

Timing = Literal["activated","triggered","static","replacement"]

@dataclass
class TargetSchema:
    zones: List[str]                # ["battlefield","stack","graveyard"]
    types: List[str]                # ["creature","planeswalker","any"]
    controller: Optional[str] = None  # "you","opponent","any"

@dataclass
class IROp:
    op: str                         # "deal","draw","destroy","scry","bounce","pump","gain_life",...
    args: Dict[str, Any]            # {"amount":"X","to":"any"} etc.

@dataclass
class IRAbility:
    timing: Timing
    condition: Dict[str, Any]       # {"event":"ETB","self":True} or {"replacement":"damage"}
    cost: List[Dict[str, Any]]      # [{"mana":"1R"},{"tap":True},{"sac":"This"}]
    effect: List[IROp]
    targets: Optional[TargetSchema] = None
    timestamp: Optional[int] = None
