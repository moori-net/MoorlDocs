$('.md-content p > a').each(function () {
    $(this).attr('target','_blank');
});

$('.md-content li > a').each(function () {
    $(this).attr('target','_blank');
});

$('.md-content a[href*="examples"]').each(function () {
    $(this).attr('download', '');
});

$('.md-content p > img').each(function () {
    let url = this.src;
    let alt = this.alt;

    $(this).wrap('<a data-fancybox="gallery" title="' + alt + '" href="' + url + '"></a>');
});

var consent = __md_get("__consent")
if (consent && consent.matomo) {
    var _paq = window._paq = window._paq || [];
    _paq.push(["setDoNotTrack", true]);
    _paq.push(['trackPageView']);
    _paq.push(['enableLinkTracking']);
    (function() {
        var u="//matomo.moori.net/";
        _paq.push(['setTrackerUrl', u+'matomo.php']);
        _paq.push(['setSiteId', '3']);
        var d=document, g=d.createElement('script'), s=d.getElementsByTagName('script')[0];
        g.async=true; g.src=u+'matomo.js'; s.parentNode.insertBefore(g,s);
    })();
}
