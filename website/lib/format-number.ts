const thinSpace = "\u202f";
const superscripts:Record<string,string>={"-":"⁻","+":"⁺","0":"⁰","1":"¹","2":"²","3":"³","4":"⁴","5":"⁵","6":"⁶","7":"⁷","8":"⁸","9":"⁹"};
/** Group exact decimal strings without passing their precision through Number. */
export function groupDecimal(value:string|number):string{
 const text=String(value),match=text.match(/^([+-]?)(\d+)(?:\.(\d+))?$/);
 if(!match)return text;
 const integer=match[2].replace(/\B(?=(\d{3})+(?!\d))/g,thinSpace);
 const fraction=match[3]?.replace(/(\d{3})(?=\d)/g,`$1${thinSpace}`);
 return `${match[1]}${integer}${fraction!==undefined?`.${fraction}`:""}`;
}
/** A rounded reading value. Callers keep the original exact string in details. */
export function readingNumber(value:string|number,significantDigits=7):string{
 const number=Number(value);
 if(!Number.isFinite(number))return String(value);
 if(number===0)return "0";
 if(Math.abs(number)<0.00001||Math.abs(number)>=10000000){
  const [coefficient,exponent]=number.toExponential(significantDigits-1).split("e");
  const trimmed=coefficient.replace(/(\.\d*?[1-9])0+$|\.0+$/, "$1");
  return `${groupDecimal(trimmed)} × 10${String(Number(exponent)).split("").map(c=>superscripts[c]||c).join("")}`;
 }
 const fractionDigits=Math.max(0,significantDigits-1-Math.floor(Math.log10(Math.abs(number))));
 const rounded=number.toFixed(Math.min(20,fractionDigits)).replace(/(\.\d*?[1-9])0+$|\.0+$/, "$1");
 return groupDecimal(rounded);
}
export function formatMeasurement(value:string):string{return value.replace(/[+-]?\d+(?:\.\d+)?/g,match=>groupDecimal(match));}
