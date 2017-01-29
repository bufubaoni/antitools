var fun = function (p, a, c, array, e, d) {
        console.log("===========p============");
        console.log(p);
        console.log("===========a============");
        console.log(a);
        console.log("===========c============");
        console.log(c);
        console.log("===========k============");
        console.log(k);
        console.log("===========e============");
        console.log(e);
        console.log("===========d============");
        console.log(d);
    //a = 62
    //c = 97
    //e = 0
    
        e = function (c) {
            return (c < a ? "" : e(parseInt(c / a))) + ((c = c % a) > 35 ? String.fromCharCode(c + 29) : c.toString(36))
        };

        if (!''.replace(/^/, String)) {
            while (c--)d[e(c)] = array[c] || e(c);
            array = [function (e) {
                return d[e]
            }];
            e = function () {
                return '\\w+'
            };
            c = 1;
        }
        while (c--)if (array[c])p = p.replace(new RegExp('\\b' + e(c) + '\\b', 'g'), array[c]);
        return p;
    };
fun('1k A={"z":4,"B":"3","D":"4.0","C":y,"u":t,"v":"x","w":["L-K.0.2","M-O.0.2","N-J.0.2","F-E.0.2","G-I.0.2","H-s.0.2","c-b.0.2","a-f.0.2","e-d.0.2","6-5.0.2","7-8.0.2","9-o.0.2","p-r.0.2","q-m.0.2","i-h.0.2","j-l.0.2","k-n.0.2","P-14.0.2","1j-1l.0.2","1n-1m.0.2","1i-1e.0.2","1d-1f.0.2","1h-1g.0.2","1w-1v.0.2","1u-1y.0.2","1x-1t.0.2","1p-1o.0.2","1q-1s.0.2","1r-1c.0.2","X-W.0.2","Y-10.0.2","Z-V.0.2","R-Q.0.2","S-U.0.2","T-18.0.2"],"17":19,"1b":1a,"16":"/12/g/3[11]/13/","15":1}||{};', 62, 97, 'jpg||webp|古惑仔|8928|17670|iieye0010|iieye0011|35049|iieye0012|iieye0008|34356|iieye0007|11203|iieye0009|16948||15028|iieye0015|iieye0016|iieye0017|18098|16560|49408|62953|iieye0013|iieye0014|16663|46772|87948|cid|cname|files|第002卷|null|bid|cInfo|bname|burl|bpic|17601|iieye0004|iieye0005|iieye0006|41546|11127|10960|iieye0001|iieye0002|iieye0003|92312|iieye0018|13888|iieye0033|iieye0034|iieye0035|17439|26660|60093|iieye0030|iieye0031|iieye0032|65963|牛佬|ps4|Vol_002|19244|status|path|finished|13878|false|35|len|74951|iieye0022|91373|35842|15288|iieye0023|iieye0021|iieye0019|var|29493|21181|iieye0020|11701|iieye0027|iieye0028|iieye0029|26875|12251|iieye0025|39592|iieye0024|iieye0026|21208'.split('|'), 0, {});
