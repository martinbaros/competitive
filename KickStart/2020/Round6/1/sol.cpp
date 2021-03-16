#include <iostream>
#include <deque>
using namespace std;

int main() {
  int t;
  cin >> t;
  for (int test = 1; test <= t; test++) {
    int p;
    cin >> p;
    int l[p];
    for (int i = 0; i < p; i++) {
      cin >> l[i];
    }
    int longest = 0;
    for (int k = 0; k < p-1; k++) {
      int ak = 2;
      int cr = l[k] - l[k+1];
      int last = l[k+1];
      for (int q = 0; q < p-k-2; q++) {
        if (l[q+k+2] == last-cr) {
          ak += 1;
          last = l[q+k+2];
        }else{
          break;
        }
      }
      if (ak>longest) {
        longest = ak;
      }
    }
    cout << "Case #" << test << ": " << longest << endl;
  }
  return 0;
}
