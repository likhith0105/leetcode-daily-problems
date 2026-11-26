class Solution:
    def canAliceWin(self, n: int) -> bool:
        remove = 10
        alice_turn = True

        while n >= remove:
            n -= remove
            remove -= 1
            alice_turn = not alice_turn

        # Loop ends when the current player cannot make a move;
        # the winner is whichever player just finished moving.
        return not alice_turn