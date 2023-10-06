library ieee;
use ieee.std_logic_1164.all;
library work;
use work.Gates.all;

entity pg is
	port(pu, pl, gu, gl: in std_logic;
		  pr, gr: out std_logic);
end entity pg;
architecture struct of pg is
	begin
		andgate_1: andgate
			port map(A => pu, B => pl, prod => pr);
		abcgate_1: abcgate
			port map(A => gu, B => pu, C => gl, abc => gr);
	end architecture struct;
	
entity carry is
	port(ai, bi, ci: in std_logic;
		  co: out std_logic);
end entity carry;
architecture struct of carry is
	begin
		Cin_map_G_1: Cin_map_G
			port map(A => ai, B => bi, C => ci, Bit0_G => co);
	end architecture struct;
	
entity sum is
	port(pi, ci: in std_logic;
	     s: out std_logic);
end entity sum;
architecture struct of sum is
	begin
		xorgate_1: xorgate
			port map(A => pi, B => ci, uneq => s);
	end architecture struct;

entity adder_32b is
	port(A, B: in std_logic_vector(31 downto 0);
		  Cin: in std_logic;
		  S: out std_logic_vector(31 downto 0);
		  Cout: out std_logic);
end entity adder_32b;

	