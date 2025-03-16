from manim import *
import numpy as np

class IntroScene(Scene):
    def construct(self):
        # Title
        title = Text("Three-Dimensional Computing", font_size=48)
        subtitle = Text("Beyond Binary Logic", font_size=32).next_to(title, DOWN)
        
        self.play(Write(title))
        self.wait(1)
        self.play(FadeIn(subtitle))
        self.wait(2)
        
        # Transition to next scene
        self.play(FadeOut(title), FadeOut(subtitle))


class BinaryProblemScene(Scene):
    def construct(self):
        # Title
        title = Text("The Limitations of Binary Computing", font_size=40)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))
        
        # Binary representation
        binary_bits = VGroup(*[
            Square(side_length=0.8).set_fill(color=[BLUE, WHITE][i % 2], opacity=0.8)
            for i in range(8)
        ]).arrange(RIGHT, buff=0.2)
        
        binary_values = VGroup(*[
            Text(str(i % 2), font_size=30).move_to(binary_bits[i])
            for i in range(8)
        ])
        
        binary_group = VGroup(binary_bits, binary_values)
        binary_label = Text("Binary: 0s and 1s", font_size=32).next_to(binary_group, UP)
        
        self.play(FadeIn(binary_group))
        self.play(Write(binary_label))
        self.wait(2)
        
        # Show limitations
        limitation1 = Text("Limited information density", font_size=30, color=YELLOW).to_edge(LEFT).shift(DOWN)
        limitation2 = Text("Only represents two states", font_size=30, color=YELLOW).next_to(limitation1, DOWN, aligned_edge=LEFT)
        limitation3 = Text("Computational inefficiency", font_size=30, color=YELLOW).next_to(limitation2, DOWN, aligned_edge=LEFT)
        
        self.play(Write(limitation1))
        self.wait(1)
        self.play(Write(limitation2))
        self.wait(1)
        self.play(Write(limitation3))
        self.wait(2)
        
        # Transition
        self.play(
            FadeOut(binary_group), FadeOut(binary_label),
            FadeOut(limitation1), FadeOut(limitation2), FadeOut(limitation3),
            FadeOut(title)
        )


class TrinaryConcept(Scene):
    def construct(self):
        # Title
        title = Text("Introducing Three-Dimensional Computing", font_size=40)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))
        
        # Show trinary states
        binary_states = VGroup(
            Square(side_length=1).set_fill(WHITE, opacity=0.8),
            Square(side_length=1).set_fill(BLUE, opacity=0.8)
        ).arrange(RIGHT, buff=0.5)
        
        binary_labels = VGroup(
            Text("0", font_size=36).move_to(binary_states[0]),
            Text("1", font_size=36).move_to(binary_states[1])
        )
        
        binary_title = Text("Binary States", font_size=32).next_to(binary_states, UP)
        binary_group = VGroup(binary_states, binary_labels, binary_title)
        
        self.play(FadeIn(binary_group))
        self.wait(1)
        
        # Transform to trinary
        trinary_states = VGroup(
            Square(side_length=1).set_fill(RED, opacity=0.8),
            Square(side_length=1).set_fill(WHITE, opacity=0.8),
            Square(side_length=1).set_fill(BLUE, opacity=0.8)
        ).arrange(RIGHT, buff=0.5)
        
        trinary_labels = VGroup(
            Text("-1", font_size=36).move_to(trinary_states[0]),
            Text("0", font_size=36).move_to(trinary_states[1]),
            Text("1", font_size=36).move_to(trinary_states[2])
        )
        
        trinary_title = Text("Trinary States", font_size=32).next_to(trinary_states, UP)
        trinary_group = VGroup(trinary_states, trinary_labels, trinary_title)
        
        self.play(
            ReplacementTransform(binary_group, trinary_group)
        )
        self.wait(2)
        
        # Benefits
        benefits = VGroup(
            Text("• More information per digit (log₂3 ≈ 1.58 bits per trit)", font_size=24),
            Text("• Logical operations with three states", font_size=24),
            Text("• Efficient computation for certain algorithms", font_size=24),
            Text("• Binary compatibility through signal flattening", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT).to_edge(LEFT).shift(DOWN)
        
        for benefit in benefits:
            self.play(FadeIn(benefit))
            self.wait(0.5)
        
        self.wait(2)
        
        # Transition
        self.play(
            FadeOut(trinary_group),
            FadeOut(benefits),
            FadeOut(title)
        )


class TrinaryLogicScene(Scene):
    def construct(self):
        # Title
        title = Text("Trinary Logic Operations", font_size=40)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))
        
        # Logic tables
        # AND table
        and_table = Table(
            [
                ["AND", "-1", "0", "1"],
                ["-1", "-1", "-1", "-1"],
                ["0", "-1", "0", "0"],
                ["1", "-1", "0", "1"]
            ],
            row_labels=[Text(""), Text("-1"), Text("0"), Text("1")],
            col_labels=[Text(""), Text("-1"), Text("0"), Text("1")],
            include_outer_lines=True
        ).scale(0.6).to_edge(LEFT)
        
        # OR table
        or_table = Table(
            [
                ["OR", "-1", "0", "1"],
                ["-1", "-1", "0", "1"],
                ["0", "0", "0", "1"],
                ["1", "1", "1", "1"]
            ],
            row_labels=[Text(""), Text("-1"), Text("0"), Text("1")],
            col_labels=[Text(""), Text("-1"), Text("0"), Text("1")],
            include_outer_lines=True
        ).scale(0.6).to_edge(RIGHT)
        
        self.play(Create(and_table))
        self.play(Create(or_table))
        self.wait(2)
        
        # NOT operation
        not_operation = VGroup(
            Text("NOT(-1) = 1", font_size=28),
            Text("NOT(0) = 0", font_size=28),
            Text("NOT(1) = -1", font_size=28)
        ).arrange(DOWN).next_to(and_table, DOWN, buff=1)
        
        self.play(Write(not_operation))
        self.wait(2)
        
        # Animation showing computation
        compute_example = VGroup(
            Text("Example: (-1) AND 1 = ?", font_size=28, color=YELLOW),
            Text("Result: -1", font_size=28, color=GREEN)
        ).arrange(DOWN).next_to(not_operation, DOWN, buff=1)
        
        self.play(Write(compute_example[0]))
        self.wait(1.5)
        
        # Highlight the cells in the table to show computation
        and_cell = and_table.get_entries((2, 4))
        self.play(and_cell.animate.set_color(GREEN))
        self.wait(1)
        self.play(Write(compute_example[1]))
        self.wait(2)
        
        # Transition
        self.play(
            FadeOut(and_table), FadeOut(or_table), 
            FadeOut(not_operation), FadeOut(compute_example),
            FadeOut(title)
        )


class SignalFlatteningScene(Scene):
    def construct(self):
        # Title
        title = Text("Signal Flattening", font_size=40)
        subtitle = Text("Binary Compatibility with Zero Overhead", font_size=32).next_to(title, DOWN)
        
        self.play(Write(title))
        self.wait(1)
        self.play(FadeIn(subtitle))
        self.wait(1.5)
        self.play(
            title.animate.to_edge(UP),
            FadeOut(subtitle)
        )
        
        # Visualization
        trinary_values = VGroup(
            Square(side_length=0.8).set_fill(RED, opacity=0.8),
            Square(side_length=0.8).set_fill(WHITE, opacity=0.8),
            Square(side_length=0.8).set_fill(BLUE, opacity=0.8)
        ).arrange(RIGHT, buff=0.5)
        
        trinary_labels = VGroup(
            Text("-1", font_size=30).move_to(trinary_values[0]),
            Text("0", font_size=30).move_to(trinary_values[1]),
            Text("1", font_size=30).move_to(trinary_values[2])
        )
        
        flattening_arrow = Arrow(start=UP, end=DOWN, color=YELLOW).next_to(trinary_values, DOWN)
        
        binary_values = VGroup(
            Square(side_length=0.8).set_fill(BLUE, opacity=0.8),
            Square(side_length=0.8).set_fill(WHITE, opacity=0.8),
            Square(side_length=0.8).set_fill(BLUE, opacity=0.8)
        ).arrange(RIGHT, buff=0.5).next_to(flattening_arrow, DOWN)
        
        binary_labels = VGroup(
            Text("1", font_size=30).move_to(binary_values[0]),
            Text("0", font_size=30).move_to(binary_values[1]),
            Text("1", font_size=30).move_to(binary_values[2])
        )
        
        flattening_text = Text("Signal Flattening: (-1 → 1)", font_size=28, color=YELLOW).next_to(flattening_arrow, RIGHT)
        
        # Display
        self.play(
            FadeIn(trinary_values),
            Write(trinary_labels)
        )
        self.wait(1.5)
        
        self.play(
            GrowArrow(flattening_arrow),
            Write(flattening_text)
        )
        self.wait(1.5)
        
        self.play(
            FadeIn(binary_values),
            Write(binary_labels)
        )
        self.wait(2)
        
        # Explanation
        explanation = VGroup(
            Text("• -1 and 1 both treated as 'true' in binary context", font_size=24),
            Text("• Zero computational overhead - happens at hardware level", font_size=24),
            Text("• Enables seamless binary software compatibility", font_size=24),
            Text("• Can be disabled for full trinary operations", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT).to_edge(LEFT).shift(DOWN * 2)
        
        for line in explanation:
            self.play(Write(line))
            self.wait(0.5)
            
        self.wait(2)
        
        # Transition
        self.play(
            FadeOut(trinary_values), FadeOut(trinary_labels),
            FadeOut(flattening_arrow), FadeOut(flattening_text),
            FadeOut(binary_values), FadeOut(binary_labels),
            FadeOut(explanation), FadeOut(title)
        )


class TrifactoryEngineScene(Scene):
    def construct(self):
        # Title
        title = Text("The Trifactory Engine", font_size=40)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))
        
        # Engine architecture
        architecture = VGroup(
            Rectangle(height=1, width=4).set_fill(color=BLUE, opacity=0.2),
            Rectangle(height=3, width=4).set_fill(color=GREEN, opacity=0.2),
            Rectangle(height=1, width=4).set_fill(color=BLUE, opacity=0.2),
        ).arrange(DOWN, buff=0.1)
        
        labels = VGroup(
            Text("Application Layer", font_size=24).move_to(architecture[0]),
            Text("Trifactory Engine", font_size=28, color=GREEN).move_to(architecture[1]),
            Text("Hardware Layer", font_size=24).move_to(architecture[2])
        )
        
        # Engine components
        components = VGroup(
            Text("Signal Flattening Unit", font_size=20),
            Text("State Management Unit", font_size=20),
            Text("Translation Layer", font_size=20),
            Text("Optimization Analyzer", font_size=20),
            Text("Execution Scheduler", font_size=20)
        ).arrange(DOWN, aligned_edge=LEFT).move_to(architecture[1])
        
        self.play(Create(architecture), Write(labels))
        self.wait(1.5)
        
        self.play(Write(components))
        self.wait(2)
        
        # Key functionalities
        functionalities = VGroup(
            Text("Key Functionalities:", font_size=28, color=YELLOW),
            Text("• Dynamic State Management", font_size=24),
            Text("• Resource Optimization", font_size=24),
            Text("• Conventional-Quantum Translation", font_size=24),
            Text("• Signal Flattening", font_size=24),
            Text("• Binary Compatibility", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT).to_edge(LEFT).shift(RIGHT * 5 + DOWN * 1)
        
        self.play(Write(functionalities[0]))
        self.wait(0.5)
        
        for i in range(1, len(functionalities)):
            self.play(Write(functionalities[i]))
            self.wait(0.5)
        
        self.wait(2)
        
        # Transition
        self.play(
            FadeOut(architecture), FadeOut(labels), 
            FadeOut(components), FadeOut(functionalities),
            FadeOut(title)
        )


class HardwareImplementationScene(Scene):
    def construct(self):
        # Title
        title = Text("Hardware Implementation", font_size=40)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))
        
        # Voltage-based implementation
        voltage_title = Text("Voltage-Based Implementation", font_size=32, color=BLUE).shift(UP * 2)
        voltage_diagram = VGroup(
            Line(start=3*LEFT, end=3*RIGHT),  # Baseline (0V)
            DashedLine(start=3*LEFT + UP, end=3*RIGHT + UP),  # +1V level
            DashedLine(start=3*LEFT - UP, end=3*RIGHT - UP),  # -1V level
            Text("0V", font_size=20).next_to(Line(start=3*LEFT, end=3*RIGHT), RIGHT),
            Text("+1V", font_size=20).next_to(DashedLine(start=3*LEFT + UP, end=3*RIGHT + UP), RIGHT),
            Text("-1V", font_size=20).next_to(DashedLine(start=3*LEFT - UP, end=3*RIGHT - UP), RIGHT),
        )
        
        voltage_labels = VGroup(
            Text("'0' State", font_size=24).next_to(voltage_diagram[0], LEFT),
            Text("'1' State", font_size=24).next_to(voltage_diagram[1], LEFT),
            Text("'-1' State", font_size=24).next_to(voltage_diagram[2], LEFT),
        )
        
        self.play(Write(voltage_title))
        self.play(Create(voltage_diagram), Write(voltage_labels))
        self.wait(2)
        
        # Circuit diagram representation
        circuit_title = Text("Trinary Memory Cell", font_size=32, color=GREEN).shift(DOWN * 2)
        
        # Simple memory cell diagram
        cell = VGroup(
            Rectangle(height=2, width=3),
            Text("TMC", font_size=24),
            Text("-1, 0, 1", font_size=20).shift(DOWN * 0.5)
        ).shift(DOWN * 2)
        
        read_write_lines = VGroup(
            Line(start=cell.get_top() + UP, end=cell.get_top()),
            Text("Read/Write", font_size=20).next_to(Line(start=cell.get_top() + UP, end=cell.get_top()), UP)
        )
        
        self.play(Write(circuit_title))
        self.play(Create(cell), Create(read_write_lines))
        self.wait(2)
        
        # Transition to spintronic implementation
        spintronic_text = Text("Spintronic Implementation: Electron Spins (↑, −, ↓)", font_size=28, color=RED).to_edge(DOWN)
        self.play(Write(spintronic_text))
        self.wait(2)
        
        # Transition
        self.play(
            FadeOut(voltage_title), FadeOut(voltage_diagram), FadeOut(voltage_labels),
            FadeOut(circuit_title), FadeOut(cell), FadeOut(read_write_lines),
            FadeOut(spintronic_text), FadeOut(title)
        )


class TriLangScene(Scene):
    def construct(self):
        # Title
        title = Text("Tri-Lang: A Trinary Programming Language", font_size=40)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))
    
        # Instead of using Code, create code manually with Text objects
        code_text = """
// Tri-Lang Example
function factorial(trit n) {
    if (n == -1) {
        return 0; // Error case in our system
    } elseif (n == 0 || n == 1) {
        return 1;
    } else {
        // Use trinary parallel multiplication
        return n * factorial(n-1);
    }
}

function main() {
    trit result = factorial(1);
    print(result); // Output: 1
}
        """
        
        # Create text with monospace font and syntax highlighting colors
        code_mobject = Text(
            code_text,
            font="Courier New",
            line_spacing=1.2
        ).scale(0.6)
        
        # Add a background rectangle
        background = SurroundingRectangle(
            code_mobject, 
            color=DARK_GREY,
            fill_opacity=0.9, 
            stroke_width=1,
            buff=0.3
        )
        
        code_group = VGroup(background, code_mobject)
        self.play(FadeIn(background), Write(code_mobject), run_time=2)
        self.wait(1)
        
        # Features
        features = VGroup(
            Text("Language Features:", font_size=28, color=YELLOW),
            Text("• Native trinary data types (trit, triword)", font_size=24),
            Text("• Extended operators for three states", font_size=24),
            Text("• Trinary control flow", font_size=24),
            Text("• Direct hardware optimization", font_size=24),
            Text("• Binary compatibility layer", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT).to_edge(LEFT).shift(RIGHT * 5 + DOWN * 1.5)
    
        self.play(Write(features[0]))
        self.wait(0.5)
    
        for i in range(1, len(features)):
            self.play(Write(features[i]))
            self.wait(0.5)
    
        self.wait(2)
    
        # Transition with a more dynamic effect
        self.play(
            code_group.animate.scale(0.5).set_opacity(0.3).shift(UP*3),
            features.animate.scale(0.5).set_opacity(0.3).shift(DOWN*3),
            title.animate.scale(0.5).set_opacity(0.3).shift(LEFT*5),
            run_time=1.5
        )
        self.play(
            FadeOut(code_group), 
            FadeOut(features), 
            FadeOut(title)
        )


class ApplicationsScene(Scene):
    def construct(self):
        # Title
        title = Text("Applications of Three-Dimensional Computing", font_size=40)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))
        
        # Applications
        vr_title = Text("VR/AR Simulation", font_size=32, color=BLUE)
        
        # Simple VR scene representation
        vr_scene = VGroup(
            ThreeDAxes(x_range=[-3, 3], y_range=[-3, 3], z_range=[-3, 3]).scale(0.3),
            Sphere(radius=0.3, fill_opacity=0.8).set_color(RED),
            Cube(side_length=0.5, fill_opacity=0.8).set_color(GREEN).shift(RIGHT + UP),
            Torus(major_radius=0.5, minor_radius=0.1, fill_opacity=0.8).set_color(BLUE).shift(LEFT + DOWN),
        )
        
        # VR Statistics
        vr_stats = VGroup(
            Text("Performance Improvements:", font_size=24, color=YELLOW),
            Text("• Frame Render Time: 26.1%", font_size=20),
            Text("• Memory Usage: 33.3%", font_size=20),
            Text("• Physics Updates: 40.4%", font_size=20),
            Text("• Power Consumption: 24.2%", font_size=20),
        ).arrange(DOWN, aligned_edge=LEFT)
        
        vr_group = VGroup(vr_title, vr_scene, vr_stats).arrange(DOWN, buff=0.5).shift(UP)
        
        # Data processing application
        data_title = Text("Data Processing & AI", font_size=32, color=GREEN)
        
        # Visualization of data processing
        data_points = VGroup(*[
            Dot(point=np.array([np.random.uniform(-2, 2), np.random.uniform(-1, 1), 0]), radius=0.05)
            for _ in range(50)
        ])
        
        # Clustering visualization
        clusters = VGroup(
            Circle(radius=0.8, color=RED).shift(LEFT * 1.5),
            Circle(radius=0.8, color=BLUE).shift(RIGHT * 1.5),
        )
        
        data_benefits = VGroup(
            Text("• Efficient clustering algorithms", font_size=20),
            Text("• Enhanced neural network processing", font_size=20),
            Text("• Trinary sort: 30-40% faster", font_size=20),
        ).arrange(DOWN, aligned_edge=LEFT)
        
        data_group = VGroup(data_title, VGroup(data_points, clusters), data_benefits).arrange(DOWN, buff=0.5).shift(DOWN * 2)
        
        # Display
        self.play(FadeIn(vr_group))
        self.wait(2)
        self.play(FadeIn(data_group))
        self.wait(2)
        
        # Transition
        self.play(
            FadeOut(vr_group), FadeOut(data_group), FadeOut(title)
        )


class QuantumComparisonScene(Scene):
    def construct(self):
        # Title
        title = Text("Comparison: Three-Dimensional vs. Quantum Computing", font_size=36)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))
        
        # Create comparison table
        table = Table(
            [
                ["Qubit", "Trit"],
                ["Superposition of |0⟩ and |1⟩", "Discrete -1, 0, and 1"],
                ["Yes", "No (but can simulate)"],
                ["High", "Low (like classical)"],
                ["Near absolute zero", "Room temperature"],
                ["Specialized hardware", "Modified standard hardware"]
            ],
            row_labels=[
                Text("Basic Unit"),
                Text("States"),
                Text("Entanglement"),
                Text("Error Rate"),
                Text("Temperature"),
                Text("Hardware")
            ],
            col_labels=[
                Text("Quantum"),
                Text("Three-Dimensional")
            ]
        ).scale(0.6)
        
        self.play(Create(table))
        self.wait(2)
        
        # Middle ground positioning
        continuum = VGroup(
            Text("Classical Binary", font_size=24).shift(LEFT * 4),
            Line(start=LEFT * 3.5, end=RIGHT * 3.5),
            Text("Three-Dimensional", font_size=24, color=GREEN),
            Text("Quantum", font_size=24).shift(RIGHT * 4),
        )
        
        arrow = Arrow(start=UP * 0.5, end=DOWN * 0.5, color=GREEN).next_to(continuum[2], UP)
        
        continuum_group = VGroup(continuum, arrow).arrange(DOWN).to_edge(DOWN, buff=1)
        
        self.play(Write(continuum_group))
        self.wait(2)
        
        # Advantage text
        advantage = Text("Three-Dimensional Computing: A practical middle ground", font_size=28, color=YELLOW).next_to(continuum_group, DOWN)
        self.play(Write(advantage))
        self.wait(2)
        
        # Transition
        self.play(
            FadeOut(table), FadeOut(continuum_group), FadeOut(advantage), FadeOut(title)
        )


class ConclusionScene(Scene):
    def construct(self):
        # Title
        title = Text("Three-Dimensional Computing", font_size=48)
        subtitle = Text("The Future of Computing", font_size=36).next_to(title, DOWN)
        
        self.play(Write(title))
        self.wait(1)
        self.play(FadeIn(subtitle))
        self.wait(1.5)
        
        self.play(
            title.animate.to_edge(UP),
            FadeOut(subtitle)
        )
        
        # Key takeaways
        takeaways = VGroup(
            Text("Key Takeaways", font_size=36, color=YELLOW),
            Text("• Extends binary computing with third state (-1, 0, 1)", font_size=28),
            Text("• Signal flattening enables seamless binary compatibility", font_size=28),
            Text("• Trifactory Engine runs on standard hardware", font_size=28),
            Text("• Significant performance benefits for VR, ML, data processing", font_size=28),
            Text("• Practical middle ground between classical and quantum", font_size=28),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        
        self.play(Write(takeaways[0]))
        self.wait(1)
        
        for i in range(1, len(takeaways)):
            self.play(FadeIn(takeaways[i]))
            self.wait(0.8)
        
        self.wait(2)
        
        # Final statement
        final = Text("Three-dimensional computing - revolutionizing computation\nwithout requiring quantum hardware", font_size=32, color=GREEN)
        self.play(FadeOut(takeaways), FadeIn(final))
        self.wait(2)
        
        # Fade out
        self.play(FadeOut(title), FadeOut(final))


class ThreeDimensionalComputingVideo(Scene):
    def construct(self):
        # Call each scene's construct method with self as argument
        IntroScene.construct(self)
        BinaryProblemScene.construct(self)
        TrinaryConcept.construct(self)
        TrinaryLogicScene.construct(self)
        SignalFlatteningScene.construct(self)
        TrifactoryEngineScene.construct(self)
        HardwareImplementationScene.construct(self)
        TriLangScene.construct(self)
        ApplicationsScene.construct(self)
        QuantumComparisonScene.construct(self)
        ConclusionScene.construct(self)
