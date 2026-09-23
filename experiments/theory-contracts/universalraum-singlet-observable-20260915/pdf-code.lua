-- Keep long literal identifiers breakable; content is unchanged.
function Code(el)
  if FORMAT:match('latex') then
    local replacements = {['\\']='\\textbackslash{}', ['~']='\\textasciitilde{}', ['^']='\\textasciicircum{}'}
    local s = el.text:gsub('[\\~^#$%%&_{}]', function(c) return replacements[c] or ('\\' .. c) end)
    return pandoc.RawInline('latex', '\\codeword{' .. s .. '}')
  end
end

function Str(el)
  -- Some supplied chat pastes contain bare, very long file names rather
  -- than inline-code spans. Keep them verbatim but allow line breaking.
  if #el.text > 55 and (el.text:find('_') or el.text:find('/')) then
    return Code(el)
  end
end

function Math(el)
  if FORMAT:match('latex') and el.mathtype == 'DisplayMath' then
    return pandoc.RawInline('latex', '\\[\\adjustbox{max width=\\linewidth}{$\\displaystyle ' .. el.text .. '$}\\]')
  end
end
