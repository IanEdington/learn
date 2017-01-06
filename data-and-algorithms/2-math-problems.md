# 1. Let \(f(n)\) and \(g(n)\) be asymptotically nonnegative functions. Using the basic definition of \(\Theta\)-notation, prove that \(max(f(n), g(n)) = \Theta(f(n), g(n))\).

\begin{equation}
\begin{split}
max(f(n), g(n)) &= \Theta(f(n) + g(n)) \
f(n) &= \Theta(f(n)) \
g(n) &= \Theta(g(n)) \
max(\Theta(g(n)), \Theta(f(n))) &= \Theta(f(n) + g(n)) \
\end{split}
\end{equation}

Since a core property of \(\Theta\) notation is that we can drop lower order terms if
\(f(n) \gt g(n)\)
drop g(n) from the right side and evaluate both site do \(\Theta(f(n))\).
This also works for the other case where
\(f(n) \lt g(n)\)
. In the case where 
\(f(n) = g(n)\)

\begin{equation}
\begin{split}
max(\Theta(g(n)), \Theta(g(n))) &= \Theta(g(n) + g(n)) \
\Theta(g(n)) &= \Theta(2g(n))
\end{split}
\end{equation}

We can also drop the constant 2 since that is also a property of \(\Theta\) notation.

# 2. Show that for any real constants a and b, where b> 0, \((n+a)^b = \Theta(n^b)\).

\begin{equation}
\begin{split}
(n+a)^b &= \Theta(n^b)
\end{split}
\end{equation}

# 3. Explain why the statement, “The running time of algorithm A is at least O.n2/,” is meaningless.
O-notation denotes an upper bound of an algorithem. It doesn't make sense to say "The running time of algorithm A is greater than it's upper bound".
