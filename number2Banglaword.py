import math
numeric_words = {
    '.': 'দশমিক',
    '0': '',
    '1': 'এক',
    '01': 'এক',
    '2': 'দুই',
    '02': 'দুই',
    '3': 'তিন',
    '03': 'তিন',
    '4': 'চার',
    '04': 'চার',
    '5': 'পাঁচ',
    '05': 'পাঁচ',
    '6': 'ছয়',
    '06': 'ছয়',
    '7': 'সাত',
    '07': 'সাত',
    '8': 'আট',
    '08': 'আট',
    '9': 'নয়',
    '09': 'নয়',
    '10': 'দশ',
    '11': 'এগারো',
    '12': 'বার',
    '13': 'তের',
    '14': 'চৌদ্দ',
    '15': 'পনের',
    '16': 'ষোল',
    '17': 'সতের',
    '18': 'আঠার',
    '19': 'উনিশ',
    '20': 'বিশ',
    '21': 'একুশ',
    '22': 'বাইশ',
    '23': 'তেইশ',
    '24': 'চব্বিশ',
    '25': 'পঁচিশ',
    '26': 'ছাব্বিশ',
    '27': 'সাতাশ',
    '28': 'আঠাশ',
    '29': 'ঊনত্রিশ',
    '30': 'ত্রিশ',
    '31': 'একত্রিশ',
    '32': 'বত্রিশ',
    '33': 'তেত্রিশ',
    '34': 'চৌত্রিশ',
    '35': 'পঁয়ত্রিশ',
    '36': 'ছত্রিশ',
    '37': 'সাঁইত্রিশ',
    '38': 'আটত্রিশ',
    '39': 'ঊনচল্লিশ',
    '40': 'চল্লিশ',
    '41': 'একচল্লিশ',
    '42': 'বিয়াল্লিশ',
    '43': 'তেতাল্লিশ',
    '44': 'চুয়াল্লিশ',
    '45': 'পঁয়তাল্লিশ',
    '46': 'ছেচল্লিশ',
    '47': 'সাতচল্লিশ',
    '48': 'আটচল্লিশ',
    '49': 'ঊনপঞ্চাশ',
    '50': 'পঞ্চাশ',
    '51': 'একান্ন',
    '52': 'বায়ান্ন',
    '53': 'তিপ্পান্ন',
    '54': 'চুয়ান্ন',
    '55': 'পঞ্চান্ন',
    '56': 'ছাপ্পান্ন',
    '57': 'সাতান্ন',
    '58': 'আটান্ন',
    '59': 'ঊনষাট',
    '60': 'ষাট',
    '61': 'একষট্টি',
    '62': 'বাষট্টি',
    '63': 'তেষট্টি',
    '64': 'চৌষট্টি',
    '65': 'পঁয়ষট্টি',
    '66': 'ছেষট্টি',
    '67': 'সাতষট্টি',
    '68': 'আটষট্টি',
    '69': 'ঊনসত্তর',
    '70': 'সত্তর',
    '71': 'একাত্তর',
    '72': 'বাহাত্তর',
    '73': 'তিয়াত্তর',
    '74': 'চুয়াত্তর',
    '75': 'পঁচাত্তর',
    '76': 'ছিয়াত্তর',
    '77': 'সাতাত্তর',
    '78': 'আটাত্তর',
    '79': 'ঊনআশি',
    '80': 'আশি',
    '81': 'একাশি',
    '82': 'বিরাশি',
    '83': 'তিরাশি',
    '84': 'চুরাশি',
    '85': 'পঁচাশি',
    '86': 'ছিয়াশি',
    '87': 'সাতাশি',
    '88': 'আটাশি',
    '89': 'ঊননব্বই',
    '90': 'নব্বই',
    '91': 'একানব্বই',
    '92': 'বিরানব্বই',
    '93': 'তিরানব্বই',
    '94': 'চুরানব্বই',
    '95': 'পঁচানব্বই',
    '96': 'ছিয়ানব্বই',
    '97': 'সাতানব্বই',
    '98': 'আটানব্বই',
    '99': 'নিরানব্বই',
    '100': 'একশো',
}

units = {
    'koti': 'কোটি',
    'lokkho': 'লক্ষ',
    'hazar': 'হাজার',
    'sotok': 'শত',
    'ekok': '',
}

def input_sanitizer(number):
    if isinstance(number, float) or isinstance(number, int) or \
            isinstance(number, str):
        if isinstance(number, str):
            try:
                if "." in number:
                    number = float(number)
                else:
                    number = int(number)
            except ValueError:
                return None
        return number
    else:
        return None


def generate_segments(number):
    """
    Generating the unit segments such as koti, lokkho
    """
    segments = dict()
    segments['koti'] = math.floor(number/10000000)
    number = number % 10000000
    segments['lokkho'] = math.floor(number/100000)
    number = number % 100000
    segments['hazar'] = math.floor(number/1000)
    number = number % 1000
    segments['sotok'] = math.floor(number/100)
    number = number % 100
    segments['ekok'] = number

    return segments


def float_int_extraction(number):
    """
    Extracting the float and int part from the passed number. The first return
    is the part before the decimal point and the rest is the fraction.
    """
    _number = str(number)
    if "." in _number:
        return tuple([int(x) for x in _number.split(".")])
    else:
        return number, None


def whole_part_word_gen(segments):
    """
    Generating the bengali word for the whole part of the number
    """
    generated_words = ''
    for segment in segments:
        if segments[segment]:
            generated_words += numeric_words[str(segments[segment])] + \
                " " + units[segment] + " "

    return generated_words[:-2]


def fraction_to_words(fraction):
    """
    Generating bengali words for the part after the decimal point
    """
    generated_words = ""
    for digit in str(fraction):
        generated_words += numeric_words[digit] + " "
    return generated_words[:-1]

def to_bn_word(number):
    """
    Takes a number and outputs the word form in Bengali for that number.
    """

    generated_words = ""
    number = input_sanitizer(number)

    whole, fraction = float_int_extraction(number)

    whole_segments = generate_segments(whole)

    generated_words = whole_part_word_gen(whole_segments)

    if fraction:
        if generated_words:
            return generated_words + " দশমিক " + fraction_to_words(fraction)
        else:
            return "দশমিক " + fraction_to_words(fraction)
    else:
        return generated_words

print(to_bn_word(12054470.456))
