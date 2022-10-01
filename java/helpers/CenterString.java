package helpers;

import java.lang.String;

public class CenterString {
    public static String centerString(String s, int size) {
        int padSize = size - s.length();
        int padStart = s.length() + padSize/2;
        s = String.format("%" + padStart + "s", s);
        s = String.format("%-" + size + "s", s);
        return s;
    }
}
