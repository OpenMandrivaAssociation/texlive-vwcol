# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/vwcol
# catalog-date 2008-08-24 14:43:48 +0200
# catalog-license lppl
# catalog-version 0.1
Name:		texlive-vwcol
Version:	0.1
Release:	6
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.1-2
+ Revision: 757494
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.1-1
+ Revision: 719898
- texlive-vwcol
- texlive-vwcol
- texlive-vwcol

