# 📖 Aion  Syntax Guide v1.0

This guide defines how to write code in the **Aion** native language. Every command interacts directly with the hardware.

## 1. Variables & Constants
- `fix`: Declares a constant (Hardware-bound values).
- `var`: Declares a mutable variable (Memory-bound values).

```aion
fix SENSOR_ID = 0xAF01
var current_mood = "calm"
