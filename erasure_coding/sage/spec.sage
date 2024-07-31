def int_to_field_vec(int_elm, dim):
    bin_rep = int_elm.binary()
    bit_len = len(bin_rep)
    return [int(bin_rep[bit_len - i - 1]) if bit_len - i - 1 >=0 else 0 for i in range(0, dim)]

def int_to_field_element(int_elm, field_gen):
    bin_rep = int_elm.binary()
    bit_len = len(bin_rep)
    field = field_gen.parent()
    return sum([int(bin_rep[bit_len - i - 1])*field_gen^i for i in range(0, bit_len)])

    current_bit =  GF_POLYNOMIAL.binary()[len(GF_POLYNOMIAL.binary())-i-1]

def field_element_into_cantor_int(field_elm):
    return ZZ(list(To_V(field_elm)), base=2)

R.<x> = GF(2)[]
GF_POLYNOMIAL = 0x1002D;
mod_poly = 0;
for i in range(0,17):
    current_bit =  GF_POLYNOMIAL.binary()[len(GF_POLYNOMIAL.binary())-i-1]
    mod_poly += int(current_bit) * x^i

F.<a> = GF(2).extension(mod_poly)

CANTOR_BASIS = [
    0x0001, 0xACCA, 0x3C0E, 0x163E, 0xC582, 0xED2E, 0x914C, 0x4012, 0x6C98, 0x10D8, 0x6A72, 0xB900,
    0xFDB8, 0xFB34, 0xFF38, 0x991E,
];


cantor_basis = [int_to_field_element(CANTOR_BASIS[i],a) for i in range(0,16)]
V, From_V, To_V = F.vector_space(base=GF(2), map=True, basis=cantor_basis)

m1 = From_V(int_to_field_vec(1, 16))
m2 = From_V(int_to_field_vec(2, 16))

Fy.<y> = F[]
message = [(0, m1), (1,m2)]
py = Fy.lagrange_polynomial(message)

assert(field_element_into_cantor_int(py(cantor_basis[1])) == 0)
assert(field_element_into_cantor_int(py(cantor_basis[1]+1)) == 3)
assert(field_element_into_cantor_int(py(cantor_basis[2])) == 14)
assert(field_element_into_cantor_int(py(cantor_basis[2]+1)) == 13)

# Data generated from reed_solomon_simd
#
#
#
# fn test_generate_test_vector() {                                                                                                            let no_of_recovery_shards : usize = 4;                                                                                                  let no_of_data_shards : usize = 2;                                                                                                                                                                                                                                              // This initializes all the needed tables.                                                                                              reed_solomon_simd::engine::DefaultEngine::new();                                                                                                                                                                                                                                // CREATE ORIGINAL                                                                                                                      let shard_bytes : usize = 64;                                                                                                                                                                                                                                                   let mut original = vec![vec![0u8; shard_bytes]; no_of_data_shards];                                                                                                                                                                                                             let mut i :u8 = 0;                                                                                                                      for original_shard in &mut original {                                                                                                       i+=1;                                                                                                                                   original_shard[0] = i;                                                                                                              }                                                                                                                                                                                                                                                                                                                                                                                                                       // ENCODE                                                                                                                               let recovery = reed_solomon_simd::encode(no_of_data_shards, no_of_recovery_shards, &original).unwrap();                                 print!("{:?}", recovery);                                                                                                                                                                                                                                                   }                                                                                                                                       
#[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,\ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [14, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,\ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [13, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]                                          
