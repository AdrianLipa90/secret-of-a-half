# SOH Half-Kernel Parabolic Disk Compactification v0.4

Status: `EXACT_PARABOLIC_QUOTIENT_BIHOLOMORPHISM / G018_G019_TRANSFER / RH_EQUIVALENT_DISK_REAL_ZERO_FORM / RH_OPEN`

Let
\[
\zeta=s-\frac12,\qquad w=\zeta^2,
\]
so that the even quotient satisfies
\[
\xi\!\left(\frac12+\zeta\right)=F(w).
\]

For \(\zeta=a+ib\),
\[
|w|+\Re w=(a^2+b^2)+(a^2-b^2)=2a^2.
\]
Hence the open critical strip descends exactly to
\[
\Omega=\left\{w:\ |w|+\Re w<\frac12\right\}.
\]
The critical line is the negative real axis \(w=-\gamma^2\); the outer strip boundaries become the parabola \(|w|+\Re w=1/2\), whose vertex is \(w=1/4\).

Define
\[
\boxed{q(w)=-\tan^2\!\left(\frac\pi2\sqrt w\right).}
\]
The sign ambiguity of \(\sqrt w\) cancels because \(\tan^2\) is even.  Writing \(\zeta=a+ib\),
\[
\left|\tan\frac{\pi\zeta}{2}\right|^2
=\frac{\cosh(\pi b)-\cos(\pi a)}{\cosh(\pi b)+\cos(\pi a)}.
\]
Thus \(|q|<1\) exactly for \(|a|<1/2\), and \(|q|=1\) on \(|a|=1/2\).  Since \(r(\zeta)=\tan(\pi\zeta/2)\) is injective on that strip and odd, squaring descends through \(w=\zeta^2\).  Therefore
\[
\boxed{q:\Omega\to\mathbb D\text{ is biholomorphic}.}
\]

Its inverse is
\[
\boxed{
w(q)=\left(\frac2\pi\arctan\sqrt{-q}\right)^2
=-\frac4{\pi^2}\operatorname{artanh}^2\sqrt q,
\qquad |q|<1.
}
\]
The squared expressions are branch independent.

On the critical line,
\[
\boxed{w=-\gamma^2\Longrightarrow q=\tanh^2\!\left(\frac{\pi\gamma}{2}\right)\in[0,1).}
\]
At the parabolic vertex \(w=1/4\), \(q=-1\).  Equivalently, with \(u=e^{i\pi\zeta}\),
\[
\boxed{q=\left(\frac{1-u}{1+u}\right)^2},
\]
which makes invariance under \(\zeta\mapsto-\zeta\) explicit because \(u\mapsto u^{-1}\).

Define the compactified quotient
\[
\mathcal F(q):=F(w(q)).
\]
All nontrivial xi zeros lie in the critical strip, hence all zeros of \(F\) lie in \(\Omega\).  Therefore
\[
\boxed{RH\iff Z(\mathcal F)\subset(0,1).}
\]
G018 proves that \(F\) has no zero for \(|w|\le1/4\), so negative real \(q\in(-1,0)\) cannot contain a zero.  Consequently
\[
\boxed{RH\iff\text{every zero of }\mathcal F\text{ in }\mathbb D\text{ is real}.}
\]
This is an exact reformulation, not a proof of RH.

The inverse majorant
\[
A(q):=-w(q)=\frac4{\pi^2}\operatorname{artanh}^2\sqrt q
\]
has nonnegative Taylor coefficients.  Hence \(|A(q)|\le A(|q|)\).  With
\[
q_{18}=\tanh^2\frac\pi4,
\]
one has \(A(q_{18})=1/4\).  G018 therefore transfers to the centered disk
\[
\boxed{\mathcal F(q)\ne0\qquad(|q|\le q_{18}).}
\]

Likewise let \(R_*\) be the canonical G019 radius defined by \(F(R_*)=2F(0)\), for which G019 proves \(\Re F(w)>0\) on \(|w|\le R_*\).  Put
\[
q_{19}=\tanh^2\!\left(\frac\pi2\sqrt{R_*}\right).
\]
Then \(|q|\le q_{19}\Rightarrow |w(q)|\le R_*\), so
\[
\boxed{\Re\mathcal F(q)>0\qquad(|q|\le q_{19}).}
\]
Numerically \(q_{18}\approx0.4300660362\), while the existing G019 value gives \(q_{19}\approx0.999999889866\).  These numbers are regression diagnostics; the transfer statements are analytic consequences of G018/G019.

Proof firewall:

- exact: strip-to-parabola identity, biholomorphism \(\Omega\leftrightarrow\mathbb D\), inverse map, exponential-Cayley form, critical-line positive-radius image;
- exact downstream of G018/G019: compactified zero-free disk and positive-real-part disk;
- exact reformulation: RH iff all compactified zeros are positive-real, equivalently real after G018;
- open: a disk Pick/PF/inner-factor theorem forcing compactified zeros to be real; G024 order three and higher; RH.
