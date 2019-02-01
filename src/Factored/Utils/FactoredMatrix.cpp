#include <AIToolbox/Factored/Utils/FactoredMatrix.hpp>

#include <AIToolbox/Utils/Core.hpp>
#include <AIToolbox/Factored/Utils/Core.hpp>

namespace AIToolbox::Factored {
    double FactoredVector::getValue(const Factors & space, const Factors & value) const {
        double retval = 0.0;
        for (const auto & e : bases) {
            const auto id = toIndexPartial(e.tag, space, value);
            retval += e.values[id];
        }
        return retval;
    }

    double FactoredVector::getValue(const Factors & space, const Factors & value, const Vector & weights) const {
        const size_t wsize = static_cast<size_t>(weights.size());
        assert(wsize == bases.size() || wsize == bases.size() + 1);

        double retval = wsize == bases.size() + 1 ? weights[wsize - 1] : 0.0;
        for (size_t i = 0; i < bases.size(); ++i) {
            const auto & e = bases[i];
            const auto id = toIndexPartial(e.tag, space, value);
            retval += e.values[id] * weights[i];
        }
        return retval;
    }

    FactoredVector & FactoredVector::operator*=(const Vector & weights) {
        const size_t wsize = static_cast<size_t>(weights.size());
        assert(wsize == bases.size() || wsize == bases.size() + 1);

        const bool add = (wsize == bases.size() + 1);
        const double toAdd = weights[wsize - 1] / bases.size();
        for (size_t i = 0; i < bases.size(); ++i) {
            bases[i].values *= weights[i];
            if (add) bases[i].values.array() += toAdd;
        }

        return *this;
    }

    FactoredVector & FactoredVector::operator*=(const double v) {
        for (auto & b : bases)
            b.values *= v;

        return *this;
    }

    FactoredVector operator*(FactoredVector lhs, const Vector & w) {
        lhs *= w;
        return lhs;
    }

    FactoredVector operator*(FactoredVector lhs, const double v) {
        lhs *= v;
        return lhs;
    }

    FactoredVector operator*(const Vector & w, FactoredVector rhs) {
        rhs *= w;
        return rhs;
    }

    FactoredVector operator*(const double v, FactoredVector rhs) {
        rhs *= v;
        return rhs;
    }

    double Factored2DMatrix::getValue(const Factors & space, const Factors & actions, const Factors & value, const Factors & action) const {
        double retval = 0.0;
        for (const auto & e : bases) {
           const auto fid = toIndexPartial(e.tag, space, value);
           const auto aid = toIndexPartial(e.actionTag, actions, action);

           retval += e.values(fid, aid);
        }
        return retval;
    }

    double Factored2DMatrix::getValue(const Factors & space, const Factors & actions, const Factors & value, const Factors & action, const Vector & weights) const {
        const size_t wsize = static_cast<size_t>(weights.size());
        assert(wsize == bases.size() || wsize == bases.size() + 1);

        double retval = wsize == bases.size() + 1 ? weights[wsize - 1] : 0.0;
        for (size_t i = 0; i < bases.size(); ++i) {
            const auto & e = bases[i];
            const auto fid = toIndexPartial(e.tag, space, value);
            const auto aid = toIndexPartial(e.actionTag, actions, action);

            retval += e.values(fid, aid) * weights[i];
        }
        return retval;
    }

    Factored2DMatrix & Factored2DMatrix::operator*=(const Vector & weights) {
        const size_t wsize = static_cast<size_t>(weights.size());
        assert(wsize == bases.size() || wsize == bases.size() + 1);

        const bool add = (wsize == bases.size() + 1);
        const double toAdd = weights[wsize - 1] / bases.size();
        for (size_t i = 0; i < bases.size(); ++i) {
            bases[i].values *= weights[i];
            if (add) bases[i].values.array() += toAdd;
        }

        return *this;
    }

    Factored2DMatrix & Factored2DMatrix::operator*=(const double v) {
        for (auto & b : bases)
            b.values *= v;

        return *this;
    }

    Factored2DMatrix operator*(Factored2DMatrix lhs, const Vector & w) {
        lhs *= w;
        return lhs;
    }

    Factored2DMatrix operator*(const Vector & w, Factored2DMatrix rhs) {
        rhs *= w;
        return rhs;
    }

    Factored2DMatrix operator*(Factored2DMatrix lhs, const double v) {
        lhs *= v;
        return lhs;
    }

    Factored2DMatrix operator*(const double v, Factored2DMatrix rhs) {
        rhs *= v;
        return rhs;
    }
}
