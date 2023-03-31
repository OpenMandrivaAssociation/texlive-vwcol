Name:		texlive-vwcol
Version:	36254
Release:	2
Summary:	Variable-width multiple text columns
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/vwcol
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/vwcol.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/vwcol.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/vwcol.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a crude environment (vwcol) for
typesetting multicolumn paragraph text of various column widths
on a single page.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/vwcol/vwcol.sty
%doc %{_texmfdistdir}/doc/latex/vwcol/README
%doc %{_texmfdistdir}/doc/latex/vwcol/vwcol.pdf
#- source
%doc %{_texmfdistdir}/source/latex/vwcol/vwcol.dtx
%doc %{_texmfdistdir}/source/latex/vwcol/vwcol.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
