import re
s=open('game.html',encoding='utf-8').read()
m=re.search(r'<script>([\s\S]*?)</script>', s)
js=m.group(1)
pairs={'(':')','{':'}','[':']'}
stack=[]; instr=None; esc=False; ok=True
for ch in js:
    if instr:
        if esc: esc=False
        elif ch=='\\': esc=True
        elif ch==instr: instr=None
        continue
    if ch in "'\"`":
        instr=ch; continue
    if ch in pairs: stack.append(pairs[ch])
    elif ch in pairs.values():
        if not stack or stack.pop()!=ch: ok=False; break
print('brackets', 'balanced' if ok and not stack else 'UNBALANCED', 'remaining=',len(stack))
# 校验关键改动
for f in ['壁画修复','周火既衰，秦承玄水','showSteleFullImage','stele_fullscreen','silkReadyDialogueShown']:
    print(f, 'present' if f in s else 'MISSING')
print('once option used:', 'opts.once' in s)
print('风雨自合壁画排序 removed:', '风雨自合壁画排序' not in s)
