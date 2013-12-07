# revision 30212
# category Package
# catalog-ctan /graphics/pgf/contrib/pxpgfmark
# catalog-date 2013-05-02 11:19:37 +0200
# catalog-license other-free
# catalog-version 0.2
Name:		texlive-pxpgfmark
Version:	0.2
Release:	4
Summary:	e-pTeX driver for PGF inter-picture connections
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pgf/contrib/pxpgfmark
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pxpgfmark.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pxpgfmark.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The distributed drivers do not support the PGF feature of
"inter-picture connections" under e-pTeX and dvipdfmx. The
package uses existing features of dvipdfmx to fix this problem.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/pxpgfmark/pxpgfmark.sty
%doc %{_texmfdistdir}/doc/latex/pxpgfmark/LICENSE
%doc %{_texmfdistdir}/doc/latex/pxpgfmark/README

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
