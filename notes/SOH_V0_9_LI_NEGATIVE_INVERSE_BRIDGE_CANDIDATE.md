# SOH v0.9 — Li / Negative-Inverse Bridge

Let \(\Omega(s)=s/(1-s)\) and \(z_L(s)=1-1/s\). Then
\[
\boxed{z_L(s)=-1/\Omega(s)}.
\]
For \(K(s)=1-\bar s\), \(z_L(K(s))=1/\overline{z_L(s)}\), hence
\[
\Re s=1/2\iff|\Omega(s)|=1\iff|z_L(s)|=1.
\]
For a reciprocal-conjugate quartet \(Q(z)=\{z,\bar z,z^{-1},\bar z^{-1}\}\), \(z=Re^{i\phi}\),
\[
L_n(Q)=4-2(R^n+R^{-n})\cos(n\phi).
\]
The local growth radius is \(\mathscr R(\rho)=\max(R,R^{-1})=e^{|B(\rho)|}\), so
\[
V(\rho)=(\log\mathscr R(\rho))^2.
\]
If \(R\ne1\), then \(\liminf_nL_n(Q)=-\infty\).

Status: SOH-L017–SOH-L023 EXACT. SOH-C005 and RH remain OPEN.
