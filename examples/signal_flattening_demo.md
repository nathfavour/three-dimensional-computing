# Signal Flattening Demonstration

This example demonstrates how signal flattening works in the three-dimensional computing architecture, allowing seamless operation on standard hardware.

## Basic Concept

Signal flattening treats -1 as functionally equivalent to 1 in most everyday computing scenarios, effectively converting trinary logic back to binary logic with zero computational overhead.

## Implementation Example

```trilang
// Initialize the Trifactory Engine with default flattening enabled
var engine = new TrifactoryEngine(FLATTENING_MODE.ENABLED);

// Create some trinary values
trit a = 1;
trit b = 0;
trit c = -1;

// With flattening enabled:
// -1 is treated as functionally equivalent to 1
// 0 remains 0

print("Binary compatibility mode (flattening ON):");
print("Value of a (1): " + a);        // Output: 1
print("Value of b (0): " + b);        // Output: 0
print("Value of c (-1): " + c);       // Output: 1 (flattened!)
print("a OR b: " + (a | b));          // Output: 1
print("b OR c: " + (b | c));          // Output: 1
print("a AND c: " + (a & c));         // Output: 1

// Disable flattening for specialized operations
engine.disableFlattening();

print("\nFull trinary mode (flattening OFF):");
print("Value of a (1): " + a);        // Output: 1
print("Value of b (0): " + b);        // Output: 0
print("Value of c (-1): " + c);       // Output: -1 (original value preserved)
print("a OR b: " + (a | b));          // Output: 1
print("b OR c: " + (b | c));          // Output: -1 (true trinary OR)
print("a AND c: " + (a & c));         // Output: -1 (true trinary AND)

// Dynamic flattening with context awareness
engine.setFlattening(FLATTENING_MODE.CONTEXT_AWARE);

function processData(triword data) {
    // For standard computing tasks, flattening is applied automatically
    if (engine.isStandardOperation()) {
        return engine.processWithFlattening(data);
    } 
    // For specialized tasks, full trinary computing is preserved
    else {
        return engine.processTripleState(data);
    }
}
```

## Zero-Cost Implementation

The signal flattening mechanism is implemented at the lowest software level with zero computational overhead:

```
// Pseudocode for the zero-cost flattening implementation
function evaluateTrit(trit value) {
    if (flatteningEnabled) {
        // Direct mapping in hardware lookup tables
        // Maps both -1 and 1 to the same binary value (1)
        // This occurs in a single cycle with no branching
        return (value != 0) ? 1 : 0;
    } else {
        // Preserve full trinary state
        return value;
    }
}
```

## Running on Standard Hardware

Signal flattening enables three-dimensional computing to run on any standard binary computer:

1. The Trifactory Engine manages the trinary state information internally
2. When interfacing with binary components, flattening occurs automatically
3. Operations remain binary-compatible while still benefiting from trinary advantages

## Benefits of Signal Flattening

1. **Immediate Compatibility**: Run existing binary software with no modifications
2. **Zero Adaptation Cost**: No need to rewrite applications for trinary logic
3. **Selective Enhancement**: Use full trinary capabilities only where beneficial
4. **Dynamic Optimization**: Seamlessly switch between modes based on task requirements
5. **No Hardware Changes**: Achieve three-dimensional computing on standard hardware
