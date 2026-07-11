%global tl_name vwcol
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2
Release:	%{tl_revision}.1
Summary:	Variable-width multiple text columns
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/vwcol
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/vwcol.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/vwcol.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/vwcol.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a crude environment (vwcol) for typesetting
multicolumn paragraph text of various column widths on a single page.

