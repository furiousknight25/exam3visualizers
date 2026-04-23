import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def plot_chart(x_vals, y_vals, title, xlabel, ylabel, color="blue"):
    """Helper function to plot sequences and partial sums."""
    fig, ax = plt.subplots(figsize=(8, 3)) # Made the chart shorter
    ax.plot(x_vals, y_vals, marker='o', linestyle='-', markersize=4, color=color)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(True, linestyle='--', alpha=0.7)
    st.pyplot(fig)

def test_for_divergence():
    st.header("1. Test for Divergence")
    st.markdown("If $\\lim_{n \\to \\infty} a_n \\neq 0$ or does not exist, then the series $\\sum a_n$ **diverges**.")
    
    # Sliders on top
    col1, col2 = st.columns(2)
    with col1:
        c = st.slider("Numerator coefficient (c)", min_value=-5.0, max_value=5.0, value=1.0, step=0.5)
    with col2:
        d = st.slider("Denominator constant (d)", min_value=1.0, max_value=10.0, value=1.0, step=1.0)

    # Side-by-side layout for graph and analysis
    plot_col, text_col = st.columns([2, 1])
    
    with plot_col:
        n_vals = np.arange(1, 101)
        a_n = (c * n_vals) / (n_vals + d)
        plot_chart(n_vals, a_n, f"Sequence terms: a_n = ({c}n) / (n + {d})", "n", "a_n", color="purple")

    with text_col:
        st.subheader("Convergence Analysis")
        limit_val = c
        if limit_val != 0:
            st.error(
                f"**Result:** Divergent.\n\n"
                f"**Why:** As $n \\to \\infty$, the terms $a_n$ approach $c = {limit_val}$. Because $\\lim_{{n \\to \\infty}} a_n \\neq 0$, "
                f"the series must diverge."
            )
        else:
            st.warning(
                f"**Result:** Inconclusive.\n\n"
                f"**Why:** Because $\\lim_{{n \\to \\infty}} a_n = 0$, the test tells us nothing. Another test is required."
            )
            
    st.markdown("---")
    st.info("💡 **Concept Check:** Think of the Test for Divergence as your 'first-pass filter'. It can only tell you if a series *diverges*. If the individual terms you are adding together don't eventually shrink down to zero, your total sum will just keep growing to infinity. But beware: just because terms shrink to zero doesn't guarantee convergence—you'll need another test to be sure!")

def geometric_series():
    st.header("2. Geometric Series")
    st.markdown("A geometric series takes the form: $\\sum_{n=1}^{\\infty} a r^{n-1}$")

    col1, col2 = st.columns(2)
    with col1:
        a = st.slider("Initial term (a)", min_value=-5.0, max_value=5.0, value=1.0, step=0.5)
    with col2:
        r = st.slider("Common ratio (r)", min_value=-2.0, max_value=2.0, value=0.5, step=0.1)

    plot_col, text_col = st.columns([2, 1])

    with plot_col:
        n_vals = np.arange(1, 51)
        terms = a * (r ** (n_vals - 1))
        s_n = np.cumsum(terms)
        plot_chart(n_vals, s_n, f"Partial Sums of Geometric Series (a={a}, r={r})", "N (number of terms)", "S_N", color="green")

    with text_col:
        st.subheader("Convergence Analysis")
        abs_r = abs(r)
        if abs_r < 1:
            S = a / (1 - r)
            st.success(
                f"**Result:** Convergent.\n\n"
                f"**Why:** $|r| = {abs_r:.1f} < 1$, so the series converges to a finite sum."
            )
            st.latex(f"S = \\frac{{a}}{{1 - r}} = {S:.4f}")
        else:
            st.error(
                f"**Result:** Divergent.\n\n"
                f"**Why:** $|r| = {abs_r:.1f} \\geq 1$, so the terms do not shrink fast enough toward zero."
            )
            
    st.markdown("---")
    st.info("💡 **Concept Check:** Geometric series are all about constant multiplicative scaling—like a bouncing ball that loses exactly half its height on every bounce. As long as the multiplier (the ratio $r$) is strictly between -1 and 1, the sequence shrinks fast enough that we can confidently calculate the exact infinite sum using a simple formula.")

def p_series():
    st.header("3. p-series")
    st.markdown("A p-series takes the form: $\\sum_{n=1}^{\\infty} \\frac{1}{n^p}$")

    p = st.slider("Power (p)", min_value=-1.0, max_value=3.0, value=2.0, step=0.1)

    plot_col, text_col = st.columns([2, 1])

    with plot_col:
        n_vals = np.arange(1, 101)
        terms = 1.0 / (n_vals ** p)
        s_n = np.cumsum(terms)
        plot_chart(n_vals, s_n, f"Partial Sums of p-series (p={p})", "N (number of terms)", "S_N", color="orange")

    with text_col:
        st.subheader("Convergence Analysis")
        if p > 1:
            st.success(
                f"**Result:** Convergent.\n\n"
                f"**Why:** $p = {p:.1f} > 1$, the terms decrease rapidly enough that their accumulation approaches a finite limit."
            )
        else:
            st.error(
                f"**Result:** Divergent.\n\n"
                f"**Why:** $p = {p:.1f} \\leq 1$, the terms do not decrease quickly enough. The sum will eventually grow to infinity."
            )

    st.markdown("---")
    st.info("💡 **Concept Check:** The p-series is the ultimate 'benchmark' test. It perfectly illustrates the boundary between converging and diverging. The harmonic series ($p=1$) shrinks to zero, but just barely too slowly, so its sum balloons to infinity. But if you increase the power by even a fraction (like $p=1.01$), it crosses the threshold, shrinks fast enough, and converges.")

def direct_comparison_test():
    st.header("4. Direct Comparison Test")
    st.markdown(r"Suppose $0 \leq a_n \leq b_n$. If $\sum b_n$ converges, $\sum a_n$ converges. If $\sum a_n$ diverges, $\sum b_n$ diverges.")

    col1, col2 = st.columns(2)
    with col1:
        p = st.slider("Power (p) for both series", min_value=0.5, max_value=3.0, value=2.0, step=0.5)
    with col2:
        c = st.slider("Constant modifier (c) for a_n", min_value=0.0, max_value=10.0, value=3.0, step=0.5)

    plot_col, text_col = st.columns([2, 1])

    with plot_col:
        n_vals = np.arange(1, 21)
        b_n = 1.0 / (n_vals ** p)
        a_n = 1.0 / (n_vals ** p + c)

        fig, ax = plt.subplots(figsize=(8, 3))
        ax.plot(n_vals, b_n, label=f"$b_n = 1/n^{{{p}}}$", color="blue", marker='o', linestyle='--')
        ax.plot(n_vals, a_n, label=f"$a_n = 1/(n^{{{p}}} + {c})$", color="red", marker='x', linestyle='-')
        
        ax.set_title(r"Visual Proof: $a_n \leq b_n$")
        ax.set_xlabel("n")
        ax.legend()
        ax.grid(True, linestyle=':', alpha=0.6)
        st.pyplot(fig)

    with text_col:
        st.subheader("Analysis")
        if c >= 0:
            st.success(rf"**Visual Proof:** $a_n \leq b_n$ for all $n$ because adding a positive constant ($c = {c}$) to the denominator makes the overall fraction smaller.")
            if p > 1:
                st.info(rf"**Result:** Convergent. $\sum b_n$ converges ($p > 1$), so $\sum a_n$ must also converge.")
            else:
                st.warning(rf"**Result:** Inconclusive. $\sum b_n$ diverges, knowing $a_n$ is smaller doesn't help.")
        else:
            st.error("If $c < 0$, then $a_n$ may be greater than $b_n$, breaking the condition.")

    st.markdown("---")
    st.info("💡 **Concept Check:** This test relies on simple bounding logic: if your series is always smaller than something finite, your series must also be finite (convergent). Conversely, if you are always larger than something infinite, you must also be infinite (divergent). It's all about finding the right known 'benchmark' series to compare your unknown series against.")

def limit_comparison_test():
    st.header("5. Limit Comparison Test")
    st.markdown("Assume $a_n = \\frac{An + B}{Cn^2 + D}$ and we test against the harmonic series $b_n = \\frac{1}{n}$.")

    col1, col2, col3, col4 = st.columns(4)
    with col1: A = st.slider("A", 1, 10, 4)
    with col2: B = st.slider("B", 1, 10, 2)
    with col3: C = st.slider("C", 1, 10, 3)
    with col4: D = st.slider("D", 1, 10, 5)

    plot_col, text_col = st.columns([2, 1])

    with plot_col:
        st.subheader("Step-by-Step Limit Computation")
        st.latex(r"\text{Find } L = \lim_{n \to \infty} \frac{a_n}{b_n}")
        st.latex(f"L = \\lim_{{n \\to \\infty}} \\frac{{\\frac{{{A}n + {B}}}{{{C}n^2 + {D}}}}}{{\\frac{{1}}{{n}}}} = \\lim_{{n \\to \\infty}} \\frac{{{A}n^2 + {B}n}}{{{C}n^2 + {D}}}")
        L_val = A / C
        st.latex(f"L = \\frac{{{A}}}{{{C}}} \\approx {L_val:.3f}")

    with text_col:
        st.subheader("Analysis")
        st.success(
            f"**Result:** Divergent.\n\n"
            f"**Why:** We found $L = {L_val:.3f}$. Since $0 < L < \\infty$, $\\sum a_n$ behaves exactly like $\\sum b_n$. "
            f"Because $b_n$ is the divergent harmonic series, $\\sum a_n$ must also diverge."
        )

    st.markdown("---")
    st.info("💡 **Concept Check:** Direct Comparison can be frustrating when the math inequalities point the wrong way. The Limit Comparison Test fixes this! It looks at the *long-term behavior* of a series. By stripping away all the messy lower-degree terms and finding a finite limit, we prove that the 'core' of the sequence behaves exactly the same as a known simpler series at infinity.")

def integral_test():
    st.header("6. Integral Test")
    st.markdown("The series converges if and only if the improper integral $\\int_{1}^{\\infty} f(x) dx$ is convergent.")

    p = st.slider("Power (p) for f(x) = 1/x^p", min_value=0.5, max_value=3.0, value=2.0, step=0.1)

    plot_col, text_col = st.columns([2, 1])

    with plot_col:
        x_continuous = np.linspace(1, 20, 500)
        y_continuous = 1.0 / (x_continuous ** p)
        n_discrete = np.arange(1, 21)
        a_n = 1.0 / (n_discrete ** p)

        fig, ax = plt.subplots(figsize=(8, 3))
        ax.fill_between(x_continuous, y_continuous, color='skyblue', alpha=0.4, label=r"$\int f(x)dx$ Area")
        ax.plot(x_continuous, y_continuous, color='blue', label=f"$f(x) = 1/x^{{{p}}}$")
        ax.bar(n_discrete, a_n, width=0.8, color='orange', alpha=0.7, align='edge', label=f"$a_n$")
        ax.set_title("Integral Test: Area vs. Discrete Sum")
        ax.legend()
        ax.grid(True, linestyle=':', alpha=0.6)
        st.pyplot(fig)

    with text_col:
        st.subheader("Analysis")
        if p > 1:
            st.success(f"**Result:** Convergent.\n\n**Why:** The integral converges to a finite value. Since the area under the curve is finite, the discrete blocks $\\sum a_n$ must also be finite.")
        else:
            st.error(f"**Result:** Divergent.\n\n**Why:** The integral diverges to infinity. Because the continuous area is infinite, the discrete sum $\\sum a_n$ must also diverge.")

    st.markdown("---")
    st.info("💡 **Concept Check:** The Integral Test beautifully bridges the gap between discrete math (sums) and continuous calculus (integrals). By replacing your discrete sequence $n$ with a continuous variable $x$, you can use the area under the curve to judge the sum. Because the discrete bars fit neatly inside the continuous curve, finite area guarantees a finite sum.")

def alternating_series_test():
    st.header("7. Alternating Series Test")
    st.markdown("Requires: 1. $b_{n+1} \\le b_n$ (decreasing) and 2. $\\lim_{n \\to \\infty} b_n = 0$")

    p = st.slider("Power (p) for b_n = 1/n^p", min_value=-1.0, max_value=3.0, value=1.0, step=0.5)

    plot_col, text_col = st.columns([2, 1])

    with plot_col:
        n_vals = np.arange(1, 31).astype(float)
        b_n = 1.0 / (n_vals ** p)
        a_n = ((-1) ** (n_vals - 1)) * b_n

        fig, ax = plt.subplots(figsize=(8, 3))
        ax.stem(n_vals, a_n, linefmt='gray', markerfmt='ro', basefmt='k-', label=r"Alternating terms $a_n$")
        ax.plot(n_vals, b_n, 'b--', alpha=0.6, label=r"Envelope $b_n$")
        ax.plot(n_vals, -b_n, 'b--', alpha=0.6)
        ax.set_title("Alternating Series: Oscillation and Envelope")
        ax.legend()
        st.pyplot(fig)

    with text_col:
        st.subheader("Condition Check")
        if p > 0:
            st.success(f"**Result:** Convergent.\n\nBoth conditions met: Envelope is decreasing ($p>0$) and approaches 0.")
        elif p == 0:
            st.error(f"**Result:** Divergent.\n\nTerms alternate between 1 and -1. Limit is not 0.")
        else:
            st.error(f"**Result:** Divergent.\n\nTerms grow as n increases. Fails both conditions.")

    st.markdown("---")
    st.info("💡 **Concept Check:** Alternating series have a built-in 'cancellation effect'. Because every other term subtracts from the total, the sum doesn't run away to infinity as easily as a standard series. As long as the steps you take keep getting smaller (decreasing) and eventually reach zero, you will eventually zigzag into a specific, finite value.")

def ratio_test():
    st.header("8. Ratio Test")
    st.markdown("Let $L = \\lim_{n \\to \\infty} \\left| \\frac{a_{n+1}}{a_n} \\right|$. Let's analyze $a_n = \\frac{n^k}{c^n}$")
    
    col1, col2 = st.columns(2)
    with col1: k = st.slider("Power (k)", 1.0, 5.0, 2.0, 1.0)
    with col2: c = st.slider("Base of Exponential (c)", 0.5, 3.0, 1.5, 0.5)

    plot_col, text_col = st.columns([2, 1])

    with plot_col:
        L_val = 1.0 / c
        n_vals = np.arange(1, 31)
        ratio_vals = (1/c) * ((n_vals + 1) / n_vals)**k
        
        fig, ax = plt.subplots(figsize=(8, 3))
        ax.plot(n_vals, ratio_vals, marker='o', color='purple', label=r"$|a_{n+1}/a_n|$")
        ax.axhline(y=1, color='red', linestyle='--', label="L = 1 (Threshold)")
        ax.axhline(y=L_val, color='green', linestyle=':', label=f"L = {L_val:.2f} (Limit)")
        ax.set_title("Convergence of the Ratio to L")
        ax.legend()
        st.pyplot(fig)

    with text_col:
        st.subheader("Calculation & Analysis")
        st.latex(f"L = \\lim_{{n \\to \\infty}} \\frac{{1}}{{{c}}} \\left( 1 + \\frac{{1}}{{n}} \\right)^{{{k}}} = \\frac{{1}}{{{c}}} \\approx {L_val:.3f}")
        
        if L_val < 1:
            st.success(f"**Result:** Convergent. $L < 1$.")
        elif L_val > 1:
            st.error(f"**Result:** Divergent. $L > 1$.")
        else:
            st.warning(f"**Result:** Inconclusive. $L = 1$. ")

    st.markdown("---")
    st.info("💡 **Concept Check:** The Ratio Test asks one fundamental question: 'In the long run, does this series behave like a converging geometric series?' By dividing the next term by the current term, we find the eventual multiplier. This test is the absolute best tool in your arsenal anytime you see factorials ($n!$) or exponential functions ($c^n$).")

def root_test():
    st.header("9. Root Test")
    st.markdown("Let $L = \\lim_{n \\to \\infty} \\sqrt[n]{|a_n|}$. Series: $a_n = \\left( \\frac{An + B}{Cn + D} \\right)^n$")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1: A = st.slider("Coeff A", 1.0, 5.0, 2.0, 0.5)
    with col2: B = st.slider("Const B", 1.0, 5.0, 1.0, 1.0)
    with col3: C = st.slider("Coeff C", 1.0, 5.0, 3.0, 0.5)
    with col4: D = st.slider("Const D", 1.0, 5.0, 2.0, 1.0)

    plot_col, text_col = st.columns([2, 1])

    with plot_col:
        L_val = abs(A / C)
        n_vals = np.arange(1, 31)
        root_vals = np.abs((A*n_vals + B) / (C*n_vals + D))
        
        fig, ax = plt.subplots(figsize=(8, 3))
        ax.plot(n_vals, root_vals, marker='s', color='teal', label=r"$\sqrt[n]{|a_n|}$")
        ax.axhline(y=1, color='red', linestyle='--', label="L = 1 (Threshold)")
        ax.axhline(y=L_val, color='green', linestyle=':', label=f"L = {L_val:.2f} (Limit)")
        ax.set_title("Convergence of the nth Root to L")
        ax.legend()
        st.pyplot(fig)

    with text_col:
        st.subheader("Calculation & Analysis")
        st.latex(f"L = \\lim_{{n \\to \\infty}} \\left| \\frac{{{A}n + {B}}}{{{C}n + {D}}} \\right| = \\frac{{{A}}}{{{C}}} \\approx {L_val:.3f}")
        
        if L_val < 1:
            st.success(f"**Result:** Convergent. $L < 1$.")
        elif L_val > 1:
            st.error(f"**Result:** Divergent. $L > 1$.")
        else:
            st.warning(f"**Result:** Inconclusive. $L = 1$. ")
            
    st.markdown("---")
    st.info("💡 **Concept Check:** Similar to the Ratio test, the Root test is hunting for geometric behavior. Taking the $n$-th root essentially strips away the exponent $n$ to reveal the core base of the sequence. If that core base is eventually less than 1, it shrinks to zero fast enough to converge. It's your go-to test anytime an entire algebraic expression is wrapped in an $n$-th power.")

def main():
    st.set_page_config(page_title="Series Convergence Tool", layout="wide")
    st.sidebar.title("Mathematical Learning Tool")
    st.sidebar.markdown("### Series Convergence Tests")
    
    module_selection = st.sidebar.radio(
        "Select a module to explore:",
        ["Test for Divergence", "Geometric Series", "p-series", "Direct Comparison Test", "Limit Comparison Test", "Integral Test", "Alternating Series Test", "Ratio Test", "Root Test"]
    )
    st.sidebar.markdown("---")
    st.sidebar.info("Adjust the sliders in each module to see how parameters affect mathematical convergence.")

    if module_selection == "Test for Divergence": test_for_divergence()
    elif module_selection == "Geometric Series": geometric_series()
    elif module_selection == "p-series": p_series()
    elif module_selection == "Direct Comparison Test": direct_comparison_test()
    elif module_selection == "Limit Comparison Test": limit_comparison_test()
    elif module_selection == "Integral Test": integral_test()
    elif module_selection == "Alternating Series Test": alternating_series_test()
    elif module_selection == "Ratio Test": ratio_test()
    elif module_selection == "Root Test": root_test()

if __name__ == "__main__":
    main()