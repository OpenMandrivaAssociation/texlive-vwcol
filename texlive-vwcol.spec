# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/vwcol
# catalog-date 2008-08-24 14:43:48 +0200
# catalog-license lppl
# catalog-version 0.1
Name:		texlive-vwcol
Version:	0.1
Release:	1
Summary:	Variable-width multiple text columns
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/vwcol
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/vwcol.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/vwcol.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/vwcol.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package provides a crude environment (vwcol) for
typesetting multicolumn paragraph text of various column widths
on a single page.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/vwcol/vwcol.sty
%doc %{_texmfdistdir}/doc/latex/vwcol/README
%doc %{_texmfdistdir}/doc/latex/vwcol/vwcol.pdf
#- source
%doc %{_texmfdistdir}/source/latex/vwcol/vwcol.dtx
%doc %{_texmfdistdir}/source/latex/vwcol/vwcol.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
