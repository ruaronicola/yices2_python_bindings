import sys

import yices_api as yapi

from .YicesException import YicesException
from .Types import Types

class Terms(object):

    NULL_TERM = -1
    TRUE      = yapi.yices_true()
    FALSE     = yapi.yices_false()
    ZERO      = yapi.yices_zero()
    ONE       = yapi.yices_int32(1)
    MINUS_ONE = yapi.yices_int32(-1)


    #general logical term constructors

    @staticmethod
    def true():
        return Terms.TRUE


    @staticmethod
    def false():
        return Terms.FALSE

    @staticmethod
    def constant(tau, index):
        retval = yapi.yices_constant(tau, index)
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_constant')
        return retval

    @staticmethod
    def new_uninterpreted_term(tau, name=None):
        term = yapi.yices_new_uninterpreted_term(tau)
        if term == Terms.NULL_TERM:
            raise YicesException('yices_new_uninterpreted_term')
        if name and not Terms.set_name(term, name):
            return None
        return term

    @staticmethod
    def new_variable(tau, name=None):
        term = yapi.yices_new_variable(tau)
        if term == Terms.NULL_TERM:
            raise YicesException('yices_new_variable')
        if name and not Terms.set_name(term, name):
            return None
        return term


    @staticmethod
    def integer(value):
        return yapi.yices_int64(long(value))


    @staticmethod
    def negation(term):
        retval = yapi.yices_not(term)
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_not')
        return retval


    @staticmethod
    def conjunction(terms):
        tlen = len(terms)
        if not len:
            return Terms.TRUE
        retval = yapi.yices_and(tlen, yapi.make_term_array(terms))
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_and')
        return retval

    @staticmethod
    def disjunction(terms):
        tlen = len(terms)
        if not len:
            return Terms.FALSE
        retval = yapi.yices_or(tlen, yapi.make_term_array(terms))
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_or')
        return retval

    @staticmethod
    def xor(terms):
        assert terms
        return yapi.yices_xor(len(terms), yapi.make_term_array(terms))

    @staticmethod
    def application(fun, terms):
        tlen = len(terms)
        assert tlen
        retval = yapi.yices_application(fun, tlen, yapi.make_term_array(terms))
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_application')
        return retval

    @staticmethod
    def ite(cond, then_term, else_term):
        retval = yapi.yices_ite(cond, then_term, else_term)
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_ite')
        return retval

    @staticmethod
    def eq(lhs_term, rhs_term):
        retval = yapi.yices_eq(lhs_term, rhs_term)
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_eq')
        return retval

    @staticmethod
    def neq(lhs_term, rhs_term):
        retval = yapi.yices_neq(lhs_term, rhs_term)
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_neq')
        return retval

    @staticmethod
    def iff(lhs_term, rhs_term):
        retval = yapi.yices_iff(lhs_term, rhs_term)
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_iff')
        return retval

    @staticmethod
    def implies(lhs_term, rhs_term):
        retval = yapi.yices_implies(lhs_term, rhs_term)
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_implies')
        return retval

    @staticmethod
    def tuple(terms):
        retval = yapi.yices_tuple(len(terms), yapi.make_term_array(terms))
        if retval == Terms.NULL_TERM:
            raise YicesException('')
        return retval

    @staticmethod
    def select(index, tuple_term):
        retval = yapi.yices_select(index, tuple_term)
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_select')
        return retval

    @staticmethod
    def tuple_update(tuple_terms, index, value):
        retval = yapi.yices_tuple_update(tuple_terms, index, value)
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_tuple_update')
        return retval

    @staticmethod
    def update(fun, args, value):
        assert args
        retval = yapi.yices_update(fun, len(args), yapi.make_term_array(args), value)
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_update')
        return retval

    @staticmethod
    def distinct(args):
        assert args
        retval = yapi.yices_distinct(len(args), yapi.make_term_array(args))
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_distinct')
        return retval

    @staticmethod
    def forall(variables, body):
        retval = yapi.yices_forall(len(variables), yapi.make_term_array(variables), body)
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_forall')
        return retval

    @staticmethod
    def exists(variables, body):
        retval = yapi.yices_exists(len(variables), yapi.make_term_array(variables), body)
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_exists')
        return retval

    #arithmetic term constructors

    @staticmethod
    def new_rational(n, d):
        assert d
        retval = yapi.yices_rational64(long(n), long(d))
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_rational64')
        return retval

    @staticmethod
    def new_rational_from_fraction(f):
        retval = yapi.yices_rational64(long(f.numerator), long(f.denominator))
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_rational64')
        return retval

    @staticmethod
    def parse_rational(s):
        assert s
        retval = yapi.yices_parse_rational(s)
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_parse_rational')
        return retval

    @staticmethod
    def parse_float(s):
        assert s
        retval = yapi.yices_parse_float(s)
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_parse_float')
        return retval

    @staticmethod
    def add(lhs, rhs):
        retval = yapi.yices_add(lhs, rhs)
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_add')
        return retval

    @staticmethod
    def sub(lhs, rhs):
        retval = yapi.yices_sub(lhs, rhs)
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_sub')
        return retval

    @staticmethod
    def mul(lhs, rhs):
        retval = yapi.yices_mul(lhs, rhs)
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_mul')
        return retval

    @staticmethod
    def neg(term):
        retval = yapi.yices_neg(term)
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_neg')
        return retval

    @staticmethod
    def square(term):
        retval = yapi.yices_square(term)
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_square')
        return retval

    @staticmethod
    def power(term, exponent):
        retval = yapi.yices_power(term, exponent)
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_power')
        return retval

    @staticmethod
    def sum(terms):
        retval = yapi.yices_sum(len(terms), yapi.make_term_array(terms))
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_sum')
        return retval

    @staticmethod
    def product(terms):
        retval = yapi.yices_product(len(terms), yapi.make_term_array(terms))
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_product')
        return retval

    @staticmethod
    def idiv(lhs, rhs):
        retval = yapi.yices_idiv(lhs, rhs)
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_idiv')
        return retval

    @staticmethod
    def imod(lhs, rhs):
        retval = yapi.yices_imod(lhs, rhs)
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_imod')
        return retval

    @staticmethod
    def divides_atom(lhs, rhs):
        retval = yapi.yices_divides_atom(lhs, rhs)
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_divides_atom')
        return retval

    @staticmethod
    def is_int_atom(term):
        retval = yapi.yices_is_int_atom(term)
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_is_int_atom')
        return retval

    @staticmethod
    def abs(term):
        retval = yapi.yices_abs(term)
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_abs')
        return retval

    @staticmethod
    def floor(term):
        retval = yapi.yices_floor(term)
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_floor')
        return retval

    @staticmethod
    def ceil(term):
        retval = yapi.yices_ceil(term)
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_ceil')
        return retval

    @staticmethod
    def arith_eq_atom(lhs, rhs):
        retval = yapi.yices_arith_eq_atom(lhs, rhs)
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_arith_eq_atom')
        return retval

    @staticmethod
    def arith_neq_atom(lhs, rhs):
        retval = yapi.yices_arith_neq_atom(lhs, rhs)
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_arith_neq_atom')
        return retval

    @staticmethod
    def arith_geq_atom(lhs, rhs):
        retval = yapi.yices_arith_geq_atom(lhs, rhs)
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_arith_geq_atom')
        return retval

    @staticmethod
    def arith_leq_atom(lhs, rhs):
        retval = yapi.yices_arith_leq_atom(lhs, rhs)
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_arith_leq_atom')
        return retval

    @staticmethod
    def arith_gt_atom(lhs, rhs):
        retval = yapi.yices_arith_gt_atom(lhs, rhs)
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_arith_gt_atom')
        return retval

    @staticmethod
    def arith_lt_atom(lhs, rhs):
        retval = yapi.yices_arith_lt_atom(lhs, rhs)
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_arith_lt_atom')
        return retval

    @staticmethod
    def arith_eq0_atom(term):
        retval = yapi.yices_arith_eq0_atom(term)
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_arith_eq0_atom')
        return retval

    @staticmethod
    def arith_neq0_atom(term):
        retval = yapi.yices_arith_neq0_atom(term)
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_arith_neq0_atom')
        return retval

    @staticmethod
    def arith_geq0_atom(term):
        retval = yapi.yices_arith_geq0_atom(term)
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_arith_geq0_atom')
        return retval

    @staticmethod
    def arith_leq0_atom(term):
        retval = yapi.yices_arith_leq0_atom(term)
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_arith_leq0_atom')
        return retval

    @staticmethod
    def arith_gt0_atom(term):
        retval = yapi.yices_arith_gt0_atom(term)
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_arith_gt0_atom')
        return retval

    @staticmethod
    def arith_lt0_atom(term):
        retval = yapi.yices_arith_lt0_atom(term)
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_arith_lt0_atom')
        return retval


    #bv term constructors

    @staticmethod
    def bv_const_integer(nbits, i):
        #FIXME: nbit needs to fit into a 32 bit int
        retval = yapi.yices_bvconst_int64(nbits, long(i))
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_bvconst_int64')
        return retval

    @staticmethod
    def bv_const_zero(nbits):
        retval = yapi.yices_bvconst_zero(nbits)
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_bvconst_zero')
        return retval

    @staticmethod
    def bv_const_one(nbits):
        retval = yapi.yices_bvconst_one(nbits)
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_bvconst_one')
        return retval

    @staticmethod
    def bv_const_minus_one(nbits):
        retval = yapi.yices_bvconst_minus_one(nbits)
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_bvconst_minus_one')
        return retval

    @staticmethod
    def bv_const_from_array(array_o_bits):
        retval = yapi.yices_bvconst_from_array(len(array_o_bits), yapi.make_int32_array(array_o_bits))
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_bvconst_from_array')
        return retval

    @staticmethod
    def parse_bvbin(s):
        retval = yapi.yices_parse_bvbin(s)
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_parse_bvbin')
        return retval

    @staticmethod
    def parse_bvhex(s):
        retval = yapi.yices_parse_bvhex(s)
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_parse_bvhex')
        return retval

    @staticmethod
    def bvadd(lhs, rhs):
        retval = yapi.yices_bvadd(lhs, rhs)
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_bvadd')
        return retval

    @staticmethod
    def bvsub(lhs, rhs):
        retval = yapi.yices_bvsub(lhs, rhs)
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_bvsub')
        return retval

    @staticmethod
    def bvneg(t):
        retval = yapi.yices_bvneg(t)
        if retval == Terms.NULL_TERM:
            raise YicesException('')
        return retval

    @staticmethod
    def bvmul(lhs, rhs):
        retval = yapi.yices_bvmul(lhs, rhs)
        if retval == Terms.NULL_TERM:
            raise YicesException('')
        return retval

    @staticmethod
    def bvsquare(t):
        retval = yapi.yices_bvsquare(t)
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_bvsquare')
        return retval

    @staticmethod
    def bvpower(t, d):
        retval = yapi.yices_bvpower(t, d)
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_bvpower')
        return retval

    @staticmethod
    def bvdiv(lhs, rhs):
        retval = yapi.yices_bvdiv(lhs, rhs)
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_bvdiv')
        return retval

    @staticmethod
    def bvrem(lhs, rhs):
        retval = yapi.yices_bvrem(lhs, rhs)
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_bvrem')
        return retval

    @staticmethod
    def bvsrem(lhs, rhs):
        retval = yapi.yices_bvsrem(lhs, rhs)
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_bvsrem')
        return retval

    @staticmethod
    def bvsmod(lhs, rhs):
        retval = yapi.yices_bvsmod(lhs, rhs)
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_bvsmod')
        return retval

    @staticmethod
    def bvnot(t):
        retval = yapi.yices_bvnot(t)
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_bvnot')
        return retval

    @staticmethod
    def bvnand(lhs, rhs):
        retval = yapi.yices_bvnand(lhs, rhs)
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_bvnand')
        return retval

    @staticmethod
    def bvnor(lhs, rhs):
        retval = yapi.yices_bvnor(lhs, rhs)
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_bvnor')
        return retval

    @staticmethod
    def bvxnor(lhs, rhs):
        retval = yapi.yices_bvxnor(lhs, rhs)
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_bvxnor')
        return retval

    @staticmethod
    def bvshl(lhs, rhs):
        retval = yapi.yices_bvshl(lhs, rhs)
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_bvshl')
        return retval

    @staticmethod
    def bvlshr(lhs, rhs):
        retval = yapi.yices_bvlshr(lhs, rhs)
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_bvlshr')
        return retval

    @staticmethod
    def bvashr(lhs, rhs):
        retval = yapi.yices_bvashr(lhs, rhs)
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_bvashr')
        return retval

    @staticmethod
    def bvand(terms):
        retval = yapi.yices_bvand(len(terms), yapi.make_term_array(terms))
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_bvand')
        return retval

    @staticmethod
    def bvor(terms):
        retval = yapi.yices_bvor(len(terms), yapi.make_term_array(terms))
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_bvor')
        return retval

    @staticmethod
    def bvxor(terms):
        retval = yapi.yices_bvxor(len(terms), yapi.make_term_array(terms))
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_bvxor')
        return retval

    @staticmethod
    def bvsum(terms):
        retval = yapi.yices_bvsum(len(terms), yapi.make_term_array(terms))
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_bvsum')
        return retval

    @staticmethod
    def bvproduct(terms):
        retval = yapi.yices_bvproduct(len(terms), yapi.make_term_array(terms))
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_bvproduct')
        return retval

    @staticmethod
    def shift_left0(t, n):
        retval = yapi.yices_shift_left0(t, n)
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_shift_left0')
        return retval

    @staticmethod
    def shift_left1(t, n):
        retval = yapi.yices_shift_left1(t, n)
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_shift_left1')
        return retval

    @staticmethod
    def shift_right0(t, n):
        retval = yapi.yices_shift_right0(t, n)
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_shift_right0')
        return retval

    @staticmethod
    def shift_right1(t, n):
        retval = yapi.yices_shift_right1(t, n)
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_shift_right1')
        return retval

    @staticmethod
    def ashift_right(t, n):
        retval = yapi.yices_ashift_right(t, n)
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_ashift_right')
        return retval

    @staticmethod
    def rotate_left(t, n):
        retval = yapi.yices_rotate_left(t, n)
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_rotate_left')
        return retval

    @staticmethod
    def rotate_right(t, n):
        retval = yapi.yices_rotate_right(t, n)
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_rotate_right')
        return retval

    @staticmethod
    def bvextract(t, i, j):
        retval = yapi.yices_bvextract(t, i, j)
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_bvextract')
        return retval

    @staticmethod
    def bvconcat(terms):
        retval = yapi.yices_bvconcat(len(terms), yapi.make_term_array(terms))
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_bvconcat')
        return retval

    @staticmethod
    def bvrepeat(t, n):
        retval = yapi.yices_bvrepeat(t, n)
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_bvrepeat')
        return retval

    @staticmethod
    def sign_extend(t, n):
        retval = yapi.yices_sign_extend(t, n)
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_sign_extend')
        return retval

    @staticmethod
    def zero_extend(t, n):
        retval = yapi.yices_zero_extend(t, n)
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_zero_extend')
        return retval

    @staticmethod
    def redand(t):
        retval = yapi.yices_redand(t)
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_redand')
        return retval

    @staticmethod
    def redor(t):
        retval = yapi.yices_redor(t)
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_redor')
        return retval

    @staticmethod
    def redcomp(lhs, rhs):
        retval = yapi.yices_redcomp(lhs, rhs)
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_redcomp')
        return retval

    @staticmethod
    def bvarray(terms):
        retval = yapi.yices_bvarray(len(terms), yapi.make_term_array(terms))
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_bvarray')
        return retval

    @staticmethod
    def bitextract(t, i):
        retval = yapi.yices_bitextract(t, i)
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_bitextract')
        return retval

    # bitvector atoms

    @staticmethod
    def bveq_atom(lhs, rhs):
        retval = yapi.yices_bveq_atom(lhs, rhs)
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_bveq_atom')
        return retval

    @staticmethod
    def bvneq_atom(lhs, rhs):
        retval = yapi.yices_bvneq_atom(lhs, rhs)
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_bvneq_atom')
        return retval

    @staticmethod
    def bvge_atom(lhs, rhs):
        retval = yapi.yices_bvge_atom(lhs, rhs)
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_bvge_atom')
        return retval

    @staticmethod
    def bvgt_atom(lhs, rhs):
        retval = yapi.yices_bvgt_atom(lhs, rhs)
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_bvgt_atom')
        return retval

    @staticmethod
    def bvle_atom(lhs, rhs):
        retval = yapi.yices_bvle_atom(lhs, rhs)
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_bvle_atom')
        return retval

    @staticmethod
    def bvlt_atom(lhs, rhs):
        retval = yapi.yices_bvlt_atom(lhs, rhs)
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_bvlt_atom')
        return retval

    @staticmethod
    def bvsge_atom(lhs, rhs):
        retval = yapi.yices_bvsge_atom(lhs, rhs)
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_bvsge_atom')
        return retval

    @staticmethod
    def bvsgt_atom(lhs, rhs):
        retval = yapi.yices_bvsgt_atom(lhs, rhs)
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_bvsgt_atom')
        return retval

    @staticmethod
    def bvsle_atom(lhs, rhs):
        retval = yapi.yices_bvsle_atom(lhs, rhs)
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_bvsle_atom')
        return retval

    @staticmethod
    def bvslt_atom(lhs, rhs):
        retval = yapi.yices_bvslt_atom(lhs, rhs)
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_bvslt_atom')
        return retval

    # parsing

    @staticmethod
    def parse_term(s):
        retval = yapi.yices_parse_term(s)
        if retval == Terms.NULL_TERM:
            raise YicesException('yices_parse_term')
        return retval


    # substitutions

    #FIXME: do these but use a dictionary rather than two arrays of the same size.

    # term recognizers

    @staticmethod
    def type_of_term(term):
        retval = yapi.yices_type_of_term(term)
        if retval == Types.NULL_TYPE:
            raise YicesException('yices_type_of_term')
        return retval

    @staticmethod
    def is_bool(term):
        retval = yapi.yices_term_is_bool(term)
        return True if retval else False

    @staticmethod
    def is_int(term):
        retval = yapi.yices_term_is_int(term)
        return True if retval else False

    @staticmethod
    def is_real(term):
        retval = yapi.yices_term_is_real(term)
        return True if retval else False

    @staticmethod
    def is_arithmetic(term):
        retval = yapi.yices_term_is_arithmetic(term)
        return True if retval else False

    @staticmethod
    def is_bitvector(term):
        retval = yapi.yices_term_is_bitvector(term)
        return True if retval else False

    @staticmethod
    def is_scalar(term):
        retval = yapi.yices_term_is_scalar(term)
        return True if retval else False

    @staticmethod
    def is_tuple(term):
        retval = yapi.yices_term_is_tuple(term)
        return True if retval else False

    @staticmethod
    def is_function(term):
        retval = yapi.yices_term_is_function(term)
        return True if retval else False

    @staticmethod
    def bitsize(term):
        retval = yapi.yices_term_bitsize(term)
        return True if retval else False

    @staticmethod
    def is_ground(term):
        retval = yapi.yices_term_is_ground(term)
        return True if retval else False


    # term deconstruction
    @staticmethod
    def is_atomic(term):
        return True if yapi.yices_term_is_atomic(term) else False

    @staticmethod
    def is_composite(term):
        return True if yapi.yices_term_is_composite(term) else False

    @staticmethod
    def is_projection(term):
        return True if yapi.yices_term_is_projection(term) else False

    @staticmethod
    def is_sum(term):
        return True if yapi.yices_term_is_sum(term) else False

    @staticmethod
    def is_bvsum(term):
        return True if yapi.yices_term_is_bvsum(term) else False

    @staticmethod
    def is_product(term):
        return True if yapi.yices_term_is_product(term) else False

    @staticmethod
    def term_constructor(term):
        retval = yapi.yices_term_constructor(term)

    @staticmethod
    def term_num_children(term):
        retval = yapi.yices_term_num_children(term)

    @staticmethod
    def term_child(term, i):
        retval = yapi.yices_term_child(term, i)

    @staticmethod
    def proj_index(term):
        retval = yapi.yices_proj_index(term)

    @staticmethod
    def proj_arg(term):
        retval = yapi.yices_proj_arg(term)


#FIXME finish these
#yices_bool_const_value(term)
#yices_bv_const_value(term)
#yices_scalar_const_value(term)
#yices_rational_const_value
#yices_sum_component
#yices_bvsum_component(term)
#yices_product_component(term)


    # names

    @staticmethod
    def set_name(term, name):
        if name is None:
            return False
        errcode = yapi.yices_set_term_name(term, name)
        if errcode == -1:
            sys.stderr.write('Terms.set_name({0}, {1}): yices_set_term_name failed {2}\n', term, name, yapi.yices_error_string())
            return False
        return True

    @staticmethod
    def remove_name(name):
        if name is None:
            return False
        yapi.yices_remove_term_name(name)
        return True


    @staticmethod
    def clear_name(term):
        errcode = yapi.yices_clear_term_name(term)
        return True if errcode == 0 else False

    @staticmethod
    def get_name(term):
        name = yapi.yices_get_term_name(term)
        if name == 0:
            return None
        return name

    @staticmethod
    def get_by_name(name):
        term = yapi.yices_get_term_by_name(name)
        if term == -1:
            return None
        return term
