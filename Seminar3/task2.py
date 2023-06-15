text = """Соображения высшего порядка, а также постоянное информационно-техническое \
 нашей деятельности играет важную роль в формировании модели развития. С другой стороны консультация\
 с профессионалами из IT способствует повышению актуальности существующих финансовых и \
 административных условий? Равным образом новая модель организационной деятельности напрямую зависит \
 от всесторонне сбалансированных нововведений. Равным образом дальнейшее развитие различных форм \
 деятельности требует от нас системного анализа экономической целесообразности принимаемых решений. \
 Равным образом рамки и место обучения кадров играет важную роль в формировании существующих \
 финансовых и административных условий. Значимость этих проблем настолько очевидна, что выбранный \
 нами инновационный путь играет важную роль в формировании форм воздействия. Повседневная практика\
  показывает, что консультация..."""
chars = {'.', ',', '!'}
text_new = "".join(filter(lambda x: x not in chars, text)).lower().split()
temp_text = {}
for var in text_new:
    if var not in temp_text:
        temp_text[var] = text_new.count(var)

text_sorted = reversed(sorted(temp_text.items(), key=lambda item: item[1]))
sorted_dict = {k: v for k, v in text_sorted}
count = 0
for key, value in sorted_dict.items():
    if count < 10:
        print(key, ':', value)
        count += 1

#print(text_sorted)
